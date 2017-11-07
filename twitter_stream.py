#-----------------------------------------------------------------------
# Elliott Miller
# Programming Assignment 2
# CS 491 with Dr. Aibek Musaev
# Due date: 9/24/2017
#-----------------------------------------------------------------------
from twitter import *

import collections
from collections import Counter
import time
import datetime
import io

try:
    import json
except ImportError:
    import simplejson as json

# set up file to write report to
f = io.open('result.txt', 'w', encoding = "utf-8")

# capture start date and time
start = datetime.datetime.now()
start_string = "<%s>\t" % start
start_string = start_string.decode('utf-8')
f.write(start_string)

# load API credentials
config = {}
execfile("config.py", config)

# create twitter API object
auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"])
stream = TwitterStream(auth = auth, secure = True)

# set current time, so that during iteration if 10 minutes has elapsed the program terminates
startTime = time.time()
PERIOD_OF_TIME = 600 #10 min

hashtags = []

# retrieve tweets from twitter public stream
tweet_iter = stream.statuses.sample()

# iterate through objects returned from stream
for tweet in tweet_iter:
    # check to make sure time has not run out
    if time.time() > startTime + PERIOD_OF_TIME : break
    # if object from stream has text attribute, then it is a tweet
    if 'text' in tweet:
        # for every hashtag that may or may not be contained in the tweet, add them to the set of hashtags (and convert to lower case)
        for hashtag in tweet['entities']['hashtags']:
        	hashtags.append(hashtag['text'].lower())


# capture end date and time
end = datetime.datetime.now()
end_string = "<%s>\n" % end
end_string = end_string.decode('utf-8')
f.write(end_string)

# use a counter class to identify the 10 most common hashtags that were tweeted during the duration of the stream
topten = Counter(hashtags).most_common(10)
# for every top ten hashtag, print its value and the number of tweets it appears in
for i in topten:
   f.write("<%s>\t<%s>\n" % (i[0], i[1]))
