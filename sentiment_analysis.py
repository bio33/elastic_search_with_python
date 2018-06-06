import csv
import re


texts=[]
output_tweets=[]
canada_woeid = 23424775

senti_wordnet = {}
def get_senti_score(text):
    # words = text.split(" ")
    words = text.split(",")
    score = []
    possitive,negative = 0,0
    for word in words:
        word = word.lower()
        if word in senti_wordnet.keys():
            score.append(senti_wordnet[word])

    for poss,neg in score:
        possitive = possitive + float(poss)
        negative = negative + float(neg)
    final_score  = possitive-negative
    if final_score > 0:
        sentiment = "possitve"
    elif final_score == 0:
        sentiment = "nuetral"
    else:
        sentiment = "negative"
    return (abs(final_score),sentiment)


# creating senti_dict
senti_wordnet = {}
with open("senti_word.txt",'r') as infile:
    line = infile.readline()
    while(line):
        word_info = line.split("\t")
        possitive = word_info[2]
        negative = word_info[3]
        words = word_info[4]
        words = words.split(" ")
        for word in words:
            if re.search("#\d",word):
                word = word[:-2]
            senti_wordnet[word]=[possitive,negative]
        line = infile.readline()


with open("processed_tweets.csv","r",encoding="utf-8") as read_tweets:
    reader = csv.reader(read_tweets,delimiter = ";")
    reader.__next__()       # ignore the header
    for row in reader:
        if row!= []:
            tweet_text = row[4]
            score,sentiment = get_senti_score(tweet_text)
            row.extend((score, sentiment))
            output_tweets.append(row[1:])

with open("Senti_tweets.csv","w",encoding="utf-8",newline="") as output:
    writer = csv.writer(output)
    writer.writerow(['id', 'user', 'created_at', "text", "score", "sentiment"])
    for tweet in output_tweets:
        writer.writerow(tweet)

