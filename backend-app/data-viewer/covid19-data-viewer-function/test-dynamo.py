import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import traceback
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


def dynamo_get_item(table_name, country):
    try:
        dynamo_table = dynamodb.Table(table_name)
        response = dynamo_table.get_item(
            Key={
                'country': country
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        print("GetItem succeeded:")
        print(json.dumps(item, indent=4, cls=DecimalEncoder))

def dynamo_query_item(table_name, country):
    try:
        print("Getting Dynamo record for-{}".format(country))
        if country is not None:
            dynamo_table = dynamodb.Table(table_name)
            response = dynamo_table.query(KeyConditionExpression = Key('country').eq(country))
            for i in response['Items']:
                print(i['country'], ":", i['total_confirmed'])
        else:
            print("Invalid data -{}".format(country))
    except Exception as e:
        print(e)
        print(traceback.print_exc())
dynamo_get_item('covid19-stats','India')