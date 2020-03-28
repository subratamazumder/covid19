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
TEMP_DOWNLOAD_LOCATION = '/tmp'
REC_TYPE_DICT = dict([(COVD19_DATA_FILE_CONFIRMED, 'total_confirmed'),(COVD19_DATA_FILE_DEATHS,'total_deaths'),(COVD19_DATA_FILE_RECOVERED,'total_recovered')])
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
def get_file_path(file_name):
    return '{}/{}'.format(TEMP_DOWNLOAD_LOCATION,file_name)
def download_s3_file(file_name):
    s3.download_file(COVD19_DATA_BUCKET, file_name, get_file_path(file_name))
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
[('country', 'india'),( rec_type ,123)]
"""
def extract_csv_line(csv_line,rec_type):
    if rec_type == 'total_confirmed':
        return dict([('country', csv_line["Country/Region"]),('total_confirmed',get_latest(csv_line))])
    if rec_type == 'total_deaths':
        return dict([('country', csv_line["Country/Region"]),('total_deaths',get_latest(csv_line))])
    if rec_type == 'total_recovered':
        return dict([('country', csv_line["Country/Region"]),('total_recovered',get_latest(csv_line))])
"""
Return rec_type as total_confirmed or total_deaths or total_recovered
"""
def get_rec_type(file_name):
    return REC_TYPE_DICT[file_name]
def prepare_db_record(file_name):
    db_record = []
    count = 0
    file_path = get_file_path(file_name)
    rec_type = get_rec_type(file_name)
    with open(file_path) as csvfile:
        for csv_line in csv.DictReader(csvfile):
            count = count + 1
            db_record[extract_csv_line(csv_line,rec_type)]
    return db_record
def write_to_dynamo(file_name):
    count = 0
    file_path = get_file_path(file_name)
    rec_type = get_rec_type(file_name)
    with open(file_path) as csvfile:
        for csv_line in csv.DictReader(csvfile):
            count = count + 1
            # Apend to bigger dictionary
            dynamo_put_item(COVD19_DYNAMO_TABLE,extract_csv_line(csv_line,rec_type),rec_type)
            if count == 1:
                break
    logger.info("Toltal number of record for -{} loaded is -{}".format(rec_type,count))
"""
Fill a big dic with all data and then write it once
"""
def dynamo_put_item(table_name,record,rec_type):
    try:
        logger.info("Puting Dynamo ecord for country-{} with rec_type-{}".format(record['country'],rec_type))
        if record['country'] is not None:
            dynamo_table = dynamodb.Table(table_name)
            dynamo_table.put_item(
                    Item=record
                )
        else:
            logger.info("Invalid data ignoring record")
    except Exception as e:
        logger.info(e)
        logger.info(traceback.print_exc())
def clean_data():
    pass
def store_covid19_data(file_name):
    download_s3_file(file_name)
    write_to_dynamo(file_name)

def lambda_handler(event, context):
    logger.info("Received event: " + json.dumps(event, indent=2))
    try:
        store_covid19_data(COVD19_DATA_FILE_CONFIRMED)
        store_covid19_data(COVD19_DATA_FILE_DEATHS)
        store_covid19_data(COVD19_DATA_FILE_RECOVERED)
        return "All covid19 data store to DynamoDB successfully"
    except Exception as e:
        logger.info(e)
        logger.info(traceback.print_exc())
        logger.info('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(COVD19_DATA_FILE_CONFIRMED, COVD19_DATA_BUCKET))
        raise e
