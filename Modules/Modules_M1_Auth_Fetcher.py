import tweepy as tw
from tweepy import OAuthHandler, StreamListener, Stream
import pandas as pd                                                    
import datetime
from multiprocessing import Process
from threading import Thread
import sys
import time

## Timer
start = time.time()

def TweetText_fetcher(keyword_tweets):
    Full_tweets= []
    tweets_text=[]
    
    for each_tweet in keyword_tweets:
        Full_tweets.append(each_tweet)
        tweets_text.append(each_tweet.full_text)

    return tweets_text

def TweetCountry_fetcher(keyword_tweets):
    tweets_location=[]
    for tweet in keyword_tweets:
        tweets_location.append(tweet.user.location)
    
    print('\nTweet Locations:\n', tweets_location)
    return tweets_location

end = (start - time.time())
#print('Time Taken By M1: ', end)