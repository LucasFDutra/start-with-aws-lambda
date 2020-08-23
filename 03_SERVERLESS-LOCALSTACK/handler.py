import json
import csv
import boto3
import os

if ('LOCALSTACK_HOSTNAME' in os.environ):
    config_s3 = {
        'service_name': 's3',
        'aws_access_key_id': '123',
        'aws_secret_access_key': '123',
        'endpoint_url': 'http://'+os.environ['LOCALSTACK_HOSTNAME']+':4566'
    }
else:
    config_s3 = {
        'service_name': 's3'
    }

s3 = boto3.client(**config_s3)

def hello(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    obj = s3.get_object(Bucket=bucket, Key=key)['Body']
    print('arquivo csv', obj)
    print('o arquivo ', key, ' chegou ao bucket ', bucket)

    response = {
        "statusCode": 200
    }
    return response