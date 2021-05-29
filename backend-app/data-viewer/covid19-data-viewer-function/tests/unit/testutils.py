import json
from datetime import datetime
import os
from zipfile import ZipFile
import boto3
import botocore
from botocore.config import Config
MAX_RETRIES = 1
BOTO3_CONFIG = Config(connect_timeout=10, read_timeout=10, retries={"max_attempts": MAX_RETRIES})

CONFIG = botocore.config.Config(retries={'max_attempts': 0})
LAMBDA_ZIP = './lambda.zip'
LOCALSTACK_ENDPOINT = 'http://localhost:4566'
DYNAMO_TABLE = 'covid-19-local-db'


def get_lambda_client():
    return boto3.client(
        'lambda',
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name='eu-west-2',
        endpoint_url=LOCALSTACK_ENDPOINT,
        config=CONFIG
    )

def get_dynamo_client():
    return boto3.client(
        'dynamodb',
        aws_access_key_id='local-key',
        aws_secret_access_key='local-secret',
        region_name='local',
        endpoint_url=LOCALSTACK_ENDPOINT,
        config= config

    )


def create_lambda_zip(function_name):
    with ZipFile(LAMBDA_ZIP, 'w') as z:
        z.write('app' + '.py')


def create_lambda(function_name):
    lambda_c = get_lambda_client()
    create_lambda_zip(function_name)
    with open(LAMBDA_ZIP, 'rb') as f:
        zipped_code = f.read()
    lambda_c.create_function(
        FunctionName=function_name,
        Runtime='python3.7',
        Role='role',
        Timeout=10,
        Handler='app.lambda_handler',
        Code=dict(ZipFile=zipped_code),
        Environment={
            "Variables": {
                "DEPLOYED_ENV": "local",
                "COVD19_DYNAMO_TABLE": DYNAMO_TABLE
            }
        }
    )
    print ("Lambda created")


def delete_lambda(function_name):
    lambda_client = get_lambda_client()
    lambda_client.delete_function(
        FunctionName=function_name
    )
    os.remove(LAMBDA_ZIP)
    print ("Lambda deleted")


def invoke_function_and_get_message(function_name):
    print("Invoking lambda")
    lambda_payload_request='{\"country\":\"India\"}'
    print("\r\nLambda request paylaod")
    print (json.dumps(lambda_payload_request, indent=4, sort_keys=True))
    lambda_client = get_lambda_client()
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=lambda_payload_request
    )
    lambda_payload_response = json.loads(
        response['Payload']
        .read()
        .decode('utf-8')
    )
    print("\r\nLambda response paylaod")
    print (json.dumps(lambda_payload_response, indent=4, sort_keys=True))
    return lambda_payload_response


def create_table(table_name):
    dynamo_client = get_dynamo_client()
    table = dynamo_client.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'country',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'country',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    print ("Table created")
    return table


def list_dynamo_table():
    dynamo_client = get_dynamo_client()
    dynamo_tables = dynamo_client.list_tables(
        # ExclusiveStartTableName=DYNAMO_TABLE,
        Limit=2)
    print ("Table listed")
    print(dynamo_tables)


def delete_table(table_name):
    dynamo_client = get_dynamo_client()
    dynamo_client.delete_table(
        TableName=table_name)
    print ("Table deleted")
    


def insert_record(table_name,record):
    # dynamo_client = get_dynamo_client()
    dynamodb = boto3.resource(
        service_name='dynamodb',
        aws_access_key_id='local_access_key',
        aws_secret_access_key='local_secret_key',
        endpoint_url='http://192.168.1.3:4566'
    )
    dynamo_table = dynamodb.Table(table_name)
    dynamo_table.put_item(
        # TableName=table_name,
        Item=record)
    print ("Record inserted")