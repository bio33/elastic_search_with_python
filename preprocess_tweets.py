
import pandas as pd
import numpy as np
import string
from nltk.corpus import stopwords
from emoji.unicode_codes import UNICODE_EMOJI
import re
from collections import Counter
from nltk.corpus import wordnet
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import re, string
from string import punctuation
from nltk.stem import WordNetLemmatizer

import re

col_Names=["id", "user", "created_at", "text"]
df = pd.read_csv("raw_tweets.csv", names=col_Names)

df=df.iloc[1:]


def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, ' ')
    return text

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
def emojireplace(tweet):
    tweet_new=emoji_pattern.sub(r'', tweet)
    return tweet_new
    
    
df["text"] = df["text"].apply(emojireplace)

def process_tweet_text(tweet):
   tweet = re.sub(r'\$\w*','',tweet) # Remove tickers
   tweet = re.sub(r'https?:\/\/.*\/\w*',' ',tweet) # Remove hyperlinks
   tweet = tweet.lower(); 
   tweet=re.sub('[^A-Za-z0-9]+', ' ', tweet)
   tweet = re.sub(r'['+string.punctuation+']+', ' ',tweet) # Remove puncutations like 's
   twtok = TweetTokenizer(strip_handles=True, reduce_len=True)
   tokens = twtok.tokenize(tweet)
   return tokens

df["text1"] = df["text"].apply(process_tweet_text)

def get_pos( word ):
    w_synsets = wordnet.synsets(word)
    pos_counts = Counter()
    pos_counts["n"] = len(  [ item for item in w_synsets if item.pos()=="n"]  )
    pos_counts["v"] = len(  [ item for item in w_synsets if item.pos()=="v"]  )
    pos_counts["a"] = len(  [ item for item in w_synsets if item.pos()=="a"]  )
    pos_counts["r"] = len(  [ item for item in w_synsets if item.pos()=="r"]  )
    most_common_pos_list = pos_counts.most_common(3)
    return most_common_pos_list[0][0]

def lemmatize_text(texts):
    s=""
    wnl = WordNetLemmatizer()
    for word in texts:
        s=s+wnl.lemmatize( word, get_pos(word) )+","
    return s

df['text1'] = df["text1"].apply(lemmatize_text)
df.drop("text", axis=1, inplace=True)

df.to_csv("processed_tweets.csv", sep=';')






   