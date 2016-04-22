from __future__ import print_function

import sys, os
import json
import logging
import string
import random
# get this file's directory independent of where it's run from
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import tweepy

log = logging.getLogger()
log.setLevel(logging.DEBUG)


CONSUMER_KEY        = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET     = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN        = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def handler(event, context):
    hexchars = string.lowercase + string.digits
    randomstring = ""
    for i in range(32):
            randomstring += hexchars[random.randint(0,len(hexchars)-1)]

    api.update_status(status=randomstring)

