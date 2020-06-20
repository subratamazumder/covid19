import json
from datetime import datetime
import os
from zipfile import ZipFile
import boto3
import botocore

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
        endpoint_url=LOCALSTACK_ENDPOINT
    )


def create_lambda_zip(function_name):
    with ZipFile(LAMBDA_ZIP, 'w') as z:
        z.write(function_name + '.py')


def create_lambda(function_name):
    lambda_c = get_lambda_client()
    create_lambda_zip(function_name)
    with open(LAMBDA_ZIP, 'rb') as f:
        zipped_code = f.read()
    lambda_c.create_function(
        FunctionName=function_name,
        Runtime='python3.7',
        Role='role',
        Handler=function_name + '.handler',
        Code=dict(ZipFile=zipped_code),
        Environment={
            "Variables": {
                "DEPLOYED_ENV": "local",
                "DYNAMO_TABLE": DYNAMO_TABLE
            }
        }
    )


def delete_lambda(function_name):
    lambda_client = get_lambda_client()
    lambda_client.delete_function(
        FunctionName=function_name
    )
    os.remove(LAMBDA_ZIP)


def invoke_function_and_get_message(function_name):
    lambda_client = get_lambda_client()
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse'
    )
    return json.loads(
        response['Payload']
        .read()
        .decode('utf-8')
    )


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
                'AttributeName': 'year',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


def list_dynamo_table():
    dynamo_client = get_dynamo_client()
    dynamo_tables = dynamo_client.list_tables(
        ExclusiveStartTableName='string',
        Limit=1)
    print(dynamo_tables)


def delete_table(table_name):
    dynamo_client = get_dynamo_client()
    dynamo_client.delete_table(
        TableName=table_name)


def insert_record(table_name,record):
    dynamo_client = get_dynamo_client()
    dynamo_client.put_item(
        TableName=table_name,
        Item=record)