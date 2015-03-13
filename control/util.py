import requests
import json
import datetime
from requests_oauthlib import OAuth1
import secrets 

def twitter_status(hashtag="fanstatus"):
    oauth = secrets.authenticate_twitter()
    request_url = "https://api.twitter.com/1.1/search/tweets.json?q=%23" + hashtag
    r = requests.get(url=request_url, auth=oauth)
    data = r.json()
    if len(data["statuses"]) >= 1:
        hashtags = data["statuses"][0]["entities"]["hashtags"]
        for tag in hashtags:
            if tag["text"].lower() == "on":
                return True
            elif tag["text"].lower() == "off":
                return False
        return None
    return None

