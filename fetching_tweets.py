import tweepy
import time
import json
import re
import csv
import  pickle
from pprint import pprint
consumer_key = "dYHPgFyXZGunx33voqaX9eZb6"
consumer_secret="flDIvtrvxNlCFiEj3nHw2RB1nNfSfxUWZmbeUC4mPO6302nAGm"
access_key="1001224103519490048-6OuynpV5LGBLIO7hLCZD8XZzyqkiM8"
access_secret="yIpbQJt3I282LJV79ho3qeoFbioiD9P5FPoeDZDa6ldVz"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api = tweepy.API(auth)


canada_woeid = 23424775
def get_profile(screen_name):
    api = tweepy.API(auth)
    try:
        user_profile = api.get_user(screen_name)

    except tweepy.error.TweepError as e:
        user_profile = json.loads(e.response.text)
    return user_profile


def get_trends(location_id):
    api = tweepy.API(auth)
    try:
        trends = api.trends_place(location_id)
    except tweepy.error.TweepError as e:
        trends = json.loads(e.response.text)
    return trends

def get_tweets(query):
    api = tweepy.API(auth)
    try:
        tweets = api.search(query,count=40)
    except tweepy.error.TweepError as e:
        tweets =[json.loads(e.response.text)]
    return tweets

queries=["Canada","Lebron","Steph Curry"]
with open("raw_tweets.csv","w",encoding="utf-8") as output:
    writer = csv.writer(output)
    writer.writerow(['id','user','created_at',"text"])
    for query in queries:
        t = get_tweets(query)
        for tweet in t[:100]:
            writer.writerow([tweet.id_str,tweet.user.screen_name,
                             tweet.created_at,tweet.text])


