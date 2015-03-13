# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs

CONSUMER_KEY = 
CONSUMER_SECRET = 
OAUTH_TOKEN = 
OAUTH_TOKEN_SECRET = 


def authenticate_twitter():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth
