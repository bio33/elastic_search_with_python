from elasticsearch import Elasticsearch
from elasticsearch import helpers
from datetime import datetime
import csv
es = Elasticsearch()
output=[]
counter =0
with open("Senti_tweets.csv","r",encoding="utf-8") as read_tweets:
    reader = csv.reader(read_tweets)
    reader.__next__()       # ignore the header
    for row in reader: 
            tweet_text = row[3]
            score,sentiment = row[4],row[5]
            output.append([counter,tweet_text,sentiment,score])
            counter = counter + 1

actions = [{
        "_index":"tweets6",
        "_type":"tweet","_id":tweet[0],
        "_source":{
        "tweet_text":tweet[1],
        "tweet_Sentiment":tweet[2],
        "tweet_score":tweet[3]
        }
} for tweet in output]

helpers.bulk(es,actions)

