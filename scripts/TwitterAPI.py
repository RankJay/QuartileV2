from requests_oauthlib import OAuth1Session
import os
import json
import requests
import time
import datetime

class DeveloperKeyConfigurations():
    # To set your enviornment variables in your terminal run the following line:

    # export 'CONSUMER_KEY'='<your_consumer_key>'
    # export 'CONSUMER_SECRET'='<your_consumer_secret>'
    # export 'BEARERTOKEN'='<your_bearer_token>'

    consumer_key = ''
    consumer_secret = ''
    bearer_token = ''
    access_token = ''
    access_secret = ''
