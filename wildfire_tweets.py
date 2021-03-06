from twitter import *
import sys

import collections
from collections import Counter
import io
import json

try:
    import json
except ImportError:
    import simplejson as json

try:
    to_unicode = unicode
except NameError:
    to_unicode = str


# set up file to write report to
f = io.open('result.txt', 'w', encoding='utf-8')

# load API credentials
config = {}
execfile("config.py", config)

# create twitter API object
oauth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"])
twitter = Twitter(auth=oauth)

tweets = []
for x in range(10):
        q = twitter.search.tweets(q='#wildfire', lang='en', count=100, include_entities='false')
        for result in q["statuses"]:
            data = {}
            data['date'] = result["created_at"]
            data['screen_name'] = result["user"]["screen_name"]
            data['tweet'] = result["text"]
            json_data = json.dumps(data)
            f.write(to_unicode(json_data))
