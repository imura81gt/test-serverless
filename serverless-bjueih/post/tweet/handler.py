from __future__ import print_function

import sys, os
import json
import logging
import string
import random
import boto3
# get this file's directory independent of where it's run from
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))
import tweepy

log = logging.getLogger()
log.setLevel(logging.DEBUG)

# tweepy
CONSUMER_KEY        = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET     = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN        = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


# s3
BUCKET_NAME         = os.environ.get('BUCKET_NAME')
s3_client = boto3.client('s3')

def handler(event, context):
    hexchars = string.lowercase + string.digits
    randomstring = ""
    for i in range(32):
            randomstring += hexchars[random.randint(0,len(hexchars)-1)]

    for record in event['Records']:
        print(record['eventID'])
        print(record['eventName'])
        print("DynamoDB Record: " + json.dumps(record['dynamodb'], indent=2))

        uid = record['dynamodb']['Keys']['Uid']['S']
        key = os.path.join(uid, "out", "movie.gif")

        tmp = os.path.join('/tmp', 'movie.gif')

        s3_client.download_file(
            BUCKET_NAME,
            key,
            tmp
        )
 
        word = uid + " " + randomstring
        #api.update_status(status=word)
        response = api.update_with_media(status=word, filename=tmp)


