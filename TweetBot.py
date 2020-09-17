""" Tweet bot that tweets every hour and replies to mentions.
    Author: Abdiel Cortes
    GitHub: AbdielCortes
    created following this YouTube video by CS Dojo:
    https://www.youtube.com/watch?v=W0wWwglE1Vc
"""

import tweepy
import time
import os
from os import environ
import TweetGenerator

#Twitter API keys; these are set as enviromental variables in Heroku
CONSUMER_KEY = environ["CONSUMER_KEY"]
CONSUMER_SECRET = environ["CONSUMER_SECRET"]
ACCESS_KEY = environ["ACCESS_KEY"]
ACCESS_SECRET = environ["ACCESS_SECRET"]

# Connecting to Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
API = tweepy.API(auth)

# Gets last seen id integer from file
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

# Stores last seen id in file
def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

# Name of the file where we're storing the id of the last tweet we replied to
LAST_SEEN_ID_FILE = "LastSeenId.txt"

# Replies to all the tweets where the bot was mentioned
def reply_to_mentions():
    # id of the last tweet that the bot replied to
    last_seen_id = retrieve_last_seen_id(LAST_SEEN_ID_FILE)

    # list containing all the tweets where the bot was mentioned
    # tweets are like dictionaries
    print("getting mentions")
    mentions = API.mentions_timeline(last_seen_id, tweet_mode='extended')

    # if we found mentions, then store the last id
    if len(mentions) > 0:
        store_last_seen_id(mentions[0].id, LAST_SEEN_ID_FILE)
        last_seen_id = mentions[0].id
        print("stored last seen id: " + str(last_seen_id))

    for mention in reversed(mentions):
        try:
            print("replying to @" + mention.user.screen_name + " with tweet id: " + str(mention.id))
            API.update_status("@" + mention.user.screen_name + " cagate en tu madre", mention.id)
        except:
            print("error when replying to mentions")

# Generates a tweet using TweetGenerator and then posts it
def tweet():
    try:
        print("tweeting")
        API.update_status(TweetGenerator.generate_tweet())
    except:
        print("error when tweeting")


while True:
    tweet()
    time.sleep(3600)
