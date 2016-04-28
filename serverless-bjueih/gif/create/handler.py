from __future__ import print_function

import json
import logging
import urllib
import boto3

log = logging.getLogger()
log.setLevel(logging.DEBUG)

s3 = boto3.client('s3')

def handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']

    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key']).decode('utf8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print('bucket:{} object:{}'.format(key, bucket))
        return key
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
