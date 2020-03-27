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
from collections import OrderedDict
from dateutil.parser import parse
patch_all()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

COVD19_DATA_SROUCE_BASE_URL = os.environ['COVD19_DATA_SROUCE_BASE_URL']
COVD19_DATA_BUCKET = os.environ['COVD19_DATA_BUCKET']
COVD19_DATA_FILE_CONFIRMED = os.environ['COVD19_DATA_FILE_CONFIRMED']
COVD19_DATA_FILE_DEATHS = os.environ['COVD19_DATA_FILE_DEATHS']
COVD19_DATA_FILE_RECOVERED = os.environ['COVD19_DATA_FILE_RECOVERED']
COVD19_DYNAMO_TABLE = os.environ['COVD19_DYNAMO_TABLE']
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
def download_s3_file(file_name):
    s3.download_file(COVD19_DATA_BUCKET, file_name, '/tmp/'+file_name)
def get_file_from_s3(file_name):
    response = s3.get_object(Bucket=COVD19_DATA_BUCKET, Key=file_name)
    logger.info("geting {} data from s3 bucket {}".format(file_name, COVD19_DATA_BUCKET))
    return response['Body'].read().decode('utf-8').split()
def get_latest(csv_line):
    dates = dict(filter(lambda element: is_date(element[0]), csv_line.items()))
    history = {date: int(amount or 0) for date, amount in dates.items()}
    latest = list(history.values())[-1]
    return latest
def calculate_total(csv_line):
   total = 0
   for item in csv_line.items(): 
      total = total + item[1]
   return total
def is_valid_record():
    pass    
def is_date(string):
   try:
      parse(string, fuzzy=False)
      return True
   except ValueError:
      return False
"""
Form a dynamo row strcuture as 
[('country', 'india'),('total_hit',123)]
"""
def extract_csv_line(csv_line):
    return dict([('country', csv_line["Country/Region"]),('total_hit',get_latest(csv_line))])
def write_to_dynamo(csv_lines):
    for csv_line in csv.DictReader(csv_lines):
        dynamo_put_item(COVD19_DYNAMO_TABLE,extract_csv_line(csv_line))
def write_to_dynamo1(file_path):
    count = 0
    with open(file_path) as csvfile:
        for csv_line in csv.DictReader(csvfile):
            count = count + 1
            dynamo_put_item(COVD19_DYNAMO_TABLE,extract_csv_line(csv_line))
    logger.info("Toltal number of record loaded -{}".format(count))
def dynamo_put_item(table_name,record):
    logger.info("Puting Dynamo ecord for country-{}".format(record['country']))
    if record['country'] is not None:
        dynamo_table = dynamodb.Table(table_name)
        dynamo_table.put_item(
                Item={
                    'country': record['country'],
                    'total_hit': record['total_hit']
                }
            )
    else:
        logger.info("Invalid data ignoring record")
def clean_data():
    pass
def store_covid19_data(file_name):
    write_to_dynamo(get_file_from_s3(file_name))
def store_covid19_data1(file_name):
    download_s3_file(file_name)
    write_to_dynamo1("/tmp/"+file_name)
def lambda_handler(event, context):
    logger.info("Received event: " + json.dumps(event, indent=2))
    try:
        store_covid19_data1(COVD19_DATA_FILE_CONFIRMED)
        # store_covid19_data(COVD19_DATA_FILE_DEATHS)
        # store_covid19_data(COVD19_DATA_FILE_RECOVERED)
        return "All covid19 data store to DynamoDB successfully"
    except Exception as e:
        logger.info(e)
        logger.info(traceback.print_exc())
        logger.info('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(COVD19_DATA_FILE_CONFIRMED, COVD19_DATA_BUCKET))
        raise e
