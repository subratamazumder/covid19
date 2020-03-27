import json
import urllib.parse
import boto3
import logging
import os
import traceback
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
import requests
patch_all()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

COVD19_DATA_SROUCE_BASE_URL = os.environ['COVD19_DATA_SROUCE_BASE_URL']
COVD19_DATA_BUCKET = os.environ['COVD19_DATA_BUCKET']
COVD19_DATA_FILE_CONFIRMED = os.environ['COVD19_DATA_FILE_CONFIRMED']
COVD19_DATA_FILE_DEATHS = os.environ['COVD19_DATA_FILE_DEATHS']
COVD19_DATA_FILE_RECOVERED = os.environ['COVD19_DATA_FILE_RECOVERED']
s3 = boto3.client('s3')
def is_data_updated(file_name):
    # Make head call
    # If response hearder says data is not modified yet then no need to download
    # Status Code: 304 Not Modified & Expires: Thu, 26 Mar 2020 16:29:52 GMT
    pass
def download_file(file_name):
    url = '{}/{}'.format(COVD19_DATA_SROUCE_BASE_URL,file_name)
    logger.info("downloading covid19 data from -{}".format(url))
    data_response = requests.get(url, allow_redirects=True)
    logger.info("status_code -{}".format(data_response.status_code))
    logger.info("Content-Type: -{}".format(data_response.headers["Content-Type"]))
    logger.info("Expires -{}".format(data_response.headers["Expires"]))
    open('/tmp/'+file_name, 'wb').write(data_response.content)

def upload_file_s3(file_name):
    s3.upload_file('/tmp/'+file_name,COVD19_DATA_BUCKET, file_name)
    logger.info("File {} uploaded successfully to bucket {}".format(file_name,COVD19_DATA_BUCKET))

def retrieve_covid19_data(file_name):
    download_file(file_name)
    upload_file_s3(file_name)

def lambda_handler(event, context):
    logger.info("Received event: " + json.dumps(event, indent=2))
    try:
        retrieve_covid19_data(COVD19_DATA_FILE_CONFIRMED)
        retrieve_covid19_data(COVD19_DATA_FILE_DEATHS)
        retrieve_covid19_data(COVD19_DATA_FILE_RECOVERED)
        return "All covid19 data loaded to S3 successfully"
    except Exception as e:
        logger.info(e)
        logger.info(traceback.print_exc())
        logger.info('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(COVD19_DATA_FILE_CONFIRMED, COVD19_DATA_BUCKET))
        raise e
