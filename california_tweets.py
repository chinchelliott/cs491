#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *
import io
import json
import sys

try:
    import json
except ImportError:
    import simplejson as json

try:
    to_unicode = unicode
except NameError:
    to_unicode = str


#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

f = io.open('cali_tweets.txt', 'w', encoding='utf-8')

#-----------------------------------------------------------------------
# perform a basic search
# Twitter API docs:
# https://dev.twitter.com/rest/reference/get/search/tweets
#-----------------------------------------------------------------------
query = twitter.search.tweets(q = "california")

#-----------------------------------------------------------------------
# How long did this query take?
#-----------------------------------------------------------------------
print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])

#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------
for result in query["statuses"]:
	data = {}
	data['date'] = result["created_at"]
	data['screen_name'] = result["user"]["screen_name"]
	data['tweet'] = result["text"]
	json_data = json.dumps(data)
	f.write(to_unicode(json_data))
