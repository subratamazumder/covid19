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
from collections import ChainMap
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
REC_TYPE_DICT = dict([(COVD19_DATA_FILE_CONFIRMED, 'total_confirmed'), (
    COVD19_DATA_FILE_DEATHS, 'total_deaths'), (COVD19_DATA_FILE_RECOVERED, 'total_recovered')])
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')


def get_file_path(file_name):
    return '{}/{}'.format(TEMP_DOWNLOAD_LOCATION, file_name)


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


def extract_csv_line(csv_line, rec_type):
    if rec_type == 'total_confirmed':
        return dict([('country', csv_line["Country/Region"]), ('total_confirmed', get_latest(csv_line))])
    if rec_type == 'total_deaths':
        return dict([('country', csv_line["Country/Region"]), ('total_deaths', get_latest(csv_line))])
    if rec_type == 'total_recovered':
        return dict([('country', csv_line["Country/Region"]), ('total_recovered', get_latest(csv_line))])


"""
Return rec_type as total_confirmed or total_deaths or total_recovered
"""


def get_rec_type(file_name):
    return REC_TYPE_DICT[file_name]

def get_total_deaths(all_db_record,country):
   unique_deaths_key = "{}#{}".format(country, 'total_deaths')
   if unique_deaths_key in all_db_record:
      return all_db_record[unique_deaths_key]
   else:
      return 0
def get_total_confirmed(all_db_record,country):
   unique_confirmed_key = "{}#{}".format(country, 'total_confirmed')
   if unique_confirmed_key in all_db_record:
      return all_db_record[unique_confirmed_key]
   else:
      return 0
def get_total_recovered(all_db_record,country):
   unique_recovered_key = "{}#{}".format(country, 'total_recovered')
   if unique_recovered_key in all_db_record:
      return all_db_record[unique_recovered_key]
   else:
      return 0
def prepare_data_record(file_name):
    all_data_record = {}
    country_list = []
    count = 0 
    rec_type = get_rec_type(file_name)
    file_path = get_file_path(file_name)
    with open(file_path) as csvfile:
        for csv_line in csv.DictReader(csvfile):
            count = count + 1
            country = csv_line["Country/Region"]
            unique_key = "{}#{}".format(country, rec_type)
            # logger.info("unique_key-{}".format(unique_key))
            if unique_key in all_data_record: #If Same country already counted before then add it up
               curr_latest = all_data_record[unique_key]
               new_latest = curr_latest + get_latest(csv_line)
               # logger.info("curr_latest-{}, new_latest-{}".format(curr_latest,new_latest))
               all_data_record[unique_key] = new_latest
            else:
               all_data_record[unique_key] = get_latest(csv_line)
               country_list.append(country)
    logger.info(
        "Toltal number of record prepared is -{}".format(count))
    return all_data_record, country_list 


def write_to_dynamo(db_record_list):
    count = 0
    for each_rec in db_record_list:
            count = count + 1
            # Apend to bigger dictionary
            dynamo_put_item(COVD19_DYNAMO_TABLE, each_rec)
            # if count == 1:
            #     break
    logger.info(
        "Toltal number of record loaded is -{}".format(count))

"""
Fill a big dic with all data and then write it once
"""


def dynamo_put_item(table_name, record):
    try:
        logger.info("Puting Dynamo record as-{}".format(record))
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
def prepare_db_record(country_list, covid19_all_data):
    dynamo_rec_list = []
    for country in country_list:
        dynamo_rec_list.append(dict([
        ('country', country),
        ('total_confirmed',get_total_confirmed(covid19_all_data,country)),
        ('total_deaths',get_total_deaths(covid19_all_data,country)),
        ('total_recovered',get_total_recovered(covid19_all_data,country))
        ]))
    return dynamo_rec_list
def store_covid19_data(file_name):
    download_s3_file(COVD19_DATA_FILE_CONFIRMED)
    download_s3_file(COVD19_DATA_FILE_DEATHS)
    download_s3_file(COVD19_DATA_FILE_RECOVERED)
    covid19_confirmed_data, covid19_confirmed_country_list = prepare_data_record(COVD19_DATA_FILE_CONFIRMED)
    covid19_deaths_data, covid19_deaths_country_list = prepare_data_record(COVD19_DATA_FILE_DEATHS)
    covid19_recovered_data, covid19_recovered_country_list = prepare_data_record(COVD19_DATA_FILE_RECOVERED)
    write_to_dynamo(prepare_db_record(covid19_confirmed_country_list,ChainMap(covid19_confirmed_data,covid19_deaths_data,covid19_recovered_data)))

def lambda_handler(event, context):
    logger.info("Received event: " + json.dumps(event, indent=2))
    try:
        store_covid19_data(COVD19_DATA_FILE_CONFIRMED)
        return "All covid19 data store to DynamoDB successfully"
    except Exception as e:
        logger.info(e)
        logger.info(traceback.print_exc())
        logger.info('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(
            COVD19_DATA_FILE_CONFIRMED, COVD19_DATA_BUCKET))
        raise e
