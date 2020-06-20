import json
import os
import pytest
from unit import testutils
from datetime import datetime
import string 
import random

DYNAMO_TABLE = 'covid-19-local-db'
FUNCTION_NAME = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
country = 'India'
total_confirmed = 123
total_deaths = 124
total_recovered = 125
last_updated_ts = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": '{ "test": "body"}',
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "queryStringParameters": {"foo": "bar"},
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "pathParameters": {"proxy": "/examplepath"},
        "httpMethod": "POST",
        "stageVariables": {"baz": "qux"},
        "path": "/examplepath",
    }

def setup():
    print('\r\nSetting up..')
    os.environ['DEPLOYED_ENV'] = 'local'
    testutils.create_lambda(FUNCTION_NAME)
    testutils.create_table(DYNAMO_TABLE)
    # testutils.list_dynamo_table()
    testutils.insert_record(DYNAMO_TABLE,
    # {'country':
    #     {
    #         'S':'India'
    #     }
    # }
        dict([
            ('country', country.upper()),
            ('total_confirmed', total_confirmed),
            ('total_deaths', total_deaths),
            ('total_recovered', total_recovered),
            ('last_updated', last_updated_ts)
        ])
    )

def teardown():
    print('\r\nTearing down..')
    testutils.delete_lambda(FUNCTION_NAME)
    testutils.delete_table(DYNAMO_TABLE)

def test_that_lambda_handler_retruns_sucess(apigw_event, mocker):
    lambda_response = testutils.invoke_function_and_get_message(FUNCTION_NAME)
    assert lambda_response["statusCode"] == 200
