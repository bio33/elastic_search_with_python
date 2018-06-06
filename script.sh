#!/bin/bash
echo "Fetching Tweets"
python fetching_tweets.py
echo "Processing Tweets"
sleep 5
python preprocess_tweets.py
echo "Performing Sentiment Analysis"
sleep 5
python sentiment_analysis.py

