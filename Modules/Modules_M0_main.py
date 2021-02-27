import tweepy as tw
from tweepy import OAuthHandler, StreamListener, Stream
import pandas as pd                                                    
import datetime
from threading import Thread
import sys
import io
from M1_Auth_Fetcher import TweetText_fetcher
from M2_URL_Emoticon_Remover import URL_Emoticon_Cleaner
from M3_SA_Handler import Sentiment_Analyzer
from M4_Tokenizer import Pos_Tokenizer, Neg_Tokenizer
from M5_POS import Pos_Tagger, Neg_Tagger
from M6_lemm_Wordlist import Pos_lemm, Neg_lemm, Wordlist
from M8_News import News
import time

## Timer
start = time.time()

def code(X):
    
    consumer_key='HJ0eUYLpsznZCHcFMj21Va1UX'
    consumer_secret='o8VyPWxlZEFv6vlmZVxnMYe2FnNcfxrYUw9Ow32eUM81VNYKlk'
    access_token='1217185233029795840-2pH6yQr8aMkCUuy8QLrjnM40poKBqU'
    access_secret='czr0hFCk8sTPMipO8zvkOkrcpEUoUSMEn7P9CuAdiponr'

    class data_listener(StreamListener):                                        #Class to print data and errors
        def on_data(self, data):
            print (data)
            return True
            
        def on_error(self, status):
            print (status)

    #Establishing Connection with Twitter API
    d_file= data_listener()                                     #Putting the captured data in variable d_file
    auth= tw.OAuthHandler(consumer_key, consumer_secret)        #Create OAuth  Handler
    auth.set_access_token(access_token, access_secret)          #Setting tokens
    api= tw.API(auth, wait_on_rate_limit=True)                  #Establishing connection through Tweepy to Twitter API i.e. 'api' is the introductory point now.
    data_pipeline= Stream(auth, d_file)

    User_word= str(X)
    keyword= User_word + '-filter:retweets'  
    keyword_tweets= tw.Cursor(api.search, q=keyword, lang='en', tweet_mode= 'extended', since=(datetime.date.today() - datetime.timedelta(days=7))).items(100)
    #print(keyword_tweets)

    
    ## M1
    Tweets_list = TweetText_fetcher(keyword_tweets)

    ## M2
    Cleaned_Tweets = URL_Emoticon_Cleaner(Tweets_list)

    ## M3
    Lists=[]
    Lists = Sentiment_Analyzer(Cleaned_Tweets)
    
    PT_list = Lists[0]
    NT_list = Lists[1]
    PT_df = Lists[2]
    NT_df = Lists[3]
    Neut_df = Lists[4]
    Pie_dict = Lists[5]
    PT_values = Lists[6]
    NT_values = Lists[7]
    #Zero_values = Lists[8]

    ## M4
    Pos_tokens = Pos_Tokenizer(PT_list, User_word)
    Neg_tokens = Neg_Tokenizer(NT_list, User_word)
    
    ##M5 (Positive)
    Pos_Tags=[]
    Pos_Tags = Pos_Tagger(Pos_tokens)
    Pnoun_list = Pos_Tags[0]
    Pverb_list = Pos_Tags[1]
    Padj_list = Pos_Tags[2]


    ##M5 (Negative)
    Neg_Tags=[]
    Neg_Tags = Neg_Tagger(Neg_tokens)
    Nnoun_list = Neg_Tags[0]
    Nverb_list = Neg_Tags[1]
    Nadj_list = Neg_Tags[2]

    ## M6
    obj9=[]
    obj9 = Pos_lemm(Pnoun_list, Pverb_list, Padj_list)
    PC_noun_words = obj9[0]
    PC_verb_words = obj9[1]
    PC_adj_words = obj9[2]


    obj10=[]
    obj10 = Neg_lemm(Nnoun_list, Nverb_list, Nadj_list)
    NC_noun_words = obj10[0]
    NC_verb_words = obj10[1]
    NC_adj_words = obj10[2]

    WC_dict = Wordlist(PC_noun_words, NC_noun_words, PC_verb_words, NC_verb_words, PC_adj_words, NC_adj_words)

    ## M8
    Recent_News = News()
    
    ## For Django API
    temp={}
    temp["Pie_Chart"] = Pie_dict
    temp["Word_Cloud"] = WC_dict
    temp["News"] = Recent_News
    

    return temp, Tweets_list, Cleaned_Tweets, PT_df, NT_df, Neut_df, PT_values, NT_values, Pos_tokens, Neg_tokens, data_pipeline

end = (start - time.time())
print('Time Taken By M0: ', end)