import json
import urllib.parse
import boto3
import logging
import os
import traceback
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
import requests
import csv
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from collections import ChainMap
from dateutil.parser import parse
patch_all()

logger = logging.getLogger()
logger.setLevel(logging.INFO)
IS_LOCAL_ENV = os.environ['DEPLOYED_ENV'] == 'local'
COVD19_DYNAMO_TABLE = os.environ['COVD19_DYNAMO_TABLE']
if IS_LOCAL_ENV:
    dynamodb = boto3.resource(
        service_name='dynamodb',
        aws_access_key_id='local_access_key',
        aws_secret_access_key='local_secret_key',
        endpoint_url='http://localhost:4566'
    )
else:
    dynamodb = boto3.resource('dynamodb')

# Helper class to convert a DynamoDB item to JSON.


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


def calculate_total(csv_line):
    total = 0
    for item in csv_line.items():
        total = total + item[1]
    return total


def is_date(string):
    try:
        parse(string, fuzzy=False)
        return True
    except ValueError:
        return False


"""
Form a dynamo row strcuture as 
"""


def fetch_covid19_data(country):
    return dynamo_get_item(COVD19_DYNAMO_TABLE, country)


"""
Fill a big dic with all data and then write it once
"""


def dynamo_get_item(table_name, country):
    try:
        dynamo_table = dynamodb.Table(table_name)
        response = dynamo_table.get_item(
            Key={
                'country': country.upper()
            }
        )
    except ClientError as e:
        logger.info(e.response['Error']['Message'])
    else:
        # logger.info(json.dumps(response, indent=4, cls=DecimalEncoder))
        if 'Item' in response:
            item = response['Item']
            logger.info("GetItem succeeded")
            logger.info(json.dumps(item, indent=4, cls=DecimalEncoder))
        else:
            logger.info("GetItem has no data:")
            raise DataNotFound("No data for country -{}".format(country))
        return item


def dynamo_query_item(table_name, country):
    try:
        logger.info("Getting Dynamo record for-{}".format(country))
        if country is not None:
            dynamo_table = dynamodb.Table(table_name)
            response = dynamo_table.query(
                KeyConditionExpression=Key('country').eq(country))
            for i in response['Items']:
                print(i['country'], ":", i['total_confirmed'])
        else:
            logger.info("Invalid data -{}".format(country))
    except Exception as e:
        logger.info(e)
        logger.info(traceback.print_exc())


def respond(err, res=None, status_code=200):
    # TODO : add 404 handling scnearios
    return {
        'statusCode': status_code if err else status_code,
        'body': err if err else json.dumps(res, indent=4, cls=DecimalEncoder),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with',
            'Access-Control-Allow-Credentials': True
        },
    }


class DataNotFound(Exception):
    """Base class for other exceptions"""
    pass


"""
path params comes as below dict format

"pathParameters": {
"country": "India"
},
"""


def lambda_handler(event, context):
    logger.info("Received event: " + json.dumps(event, indent=2))
    try:
        if 'country' in event:
            country = event['country']
        else:
            country = event['pathParameters']['country']
        return respond(None, fetch_covid19_data(country))
    except DataNotFound as e:
        logger.info(e)
        logger.info(traceback.print_exc())
        logger.info('Error getting covid19 data from table {}'.format(
            COVD19_DYNAMO_TABLE))
        return respond("{\"Error\" : \"Stats not available\"}", None, 404)
    except Exception as e:
        logger.info(e)
        logger.info(traceback.print_exc())
        logger.info('Error getting covid19 data from table {}'.format(
            COVD19_DYNAMO_TABLE))
        return respond("{\"Error\" : \"Lambda Handler Failed\"}", None, 500)
