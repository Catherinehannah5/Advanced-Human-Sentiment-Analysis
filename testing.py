import tweepy as tw
from tweepy import OAuthHandler
from tweepy import StreamListener                               
# Basic Listener that prints out the data
from tweepy import Stream  
import re 
import pandas as pd                                  
# Establishes a streaming session and routes messages to StreamListener
import datetime
import numpy as np
import pandas as pd
from PIL import Image
import itertools
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize, pos_tag, bigrams
from nltk.tokenize import TweetTokenizer
from string import punctuation
import collections
import spacy
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from rake_nltk import Rake

#Connect with Twitter API
consumer_key='HJ0eUYLpsznZCHcFMj21Va1UX'
consumer_secret='o8VyPWxlZEFv6vlmZVxnMYe2FnNcfxrYUw9Ow32eUM81VNYKlk'
access_token='1217185233029795840-2pH6yQr8aMkCUuy8QLrjnM40poKBqU'
access_secret='czr0hFCk8sTPMipO8zvkOkrcpEUoUSMEn7P9CuAdiponr'

class data_listener(StreamListener):                            #Class to print data and errors
 
    def on_data(self, data):
        print (data)
        return True
    
    def on_error(self, status):
        print (status)

d_file= data_listener()                                     #Putting the captured data in variable d_file
auth= tw.OAuthHandler(consumer_key, consumer_secret)        #Create OAuth  Handler
auth.set_access_token(access_token, access_secret)          #Setting tokens
api= tw.API(auth, wait_on_rate_limit=True)                  #Establishing connection through Tweepy to Twitter API i.e. 'api' is the introductory point now.
data_pipeline= Stream(auth, d_file) 

User_word='trump' ##*******Keyword path******
keyword= User_word + '-filter:retweets'  #Filter:Media for images and videos 
keyword_tweets= tw.Cursor(api.search, q=keyword, lang='en', tweet_mode= 'extended', since=(datetime.date.today() - datetime.timedelta(days=7))).items(100)
    ##Return a object , so python list comprehension has been used to collect object elements contained within that iterator as list
    #print([each_tweet.created_at for each_tweet in keyword_tweets])

    #Create a list and append all the tweets with all information
Full_tweets= []
tweets_text=[]
tweets_location=[]
for each_tweet in keyword_tweets:
    Full_tweets.append(each_tweet)
    tweets_text.append(each_tweet.full_text)
    tweets_location.append(each_tweet.user.location)
# print(Full_tweets)
# print('+++++++++++++++++++++++++++++++++++++++++++++++')
# print(tweets_text)
# print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
# print(tweets_location)

#Creating a dataframe
df_tweets=pd.DataFrame({'Text': tweets_text, 'Country': tweets_location})
# print(df_tweets)
# print('\n\n')
#Filter tweet texts and 
df_Text= df_tweets.iloc[:,0]        #Text Dataframe
df_Text= df_Text.str.strip()        #Removing spaces

df_Country= df_tweets.iloc[:,1]     #Country Dataframe
df_Country= df_Country.str.strip()  #Removing Spaces
# print(df_Text)
# print(df_Country)

df_Text= df_Text.replace(to_replace=r'https?:\/\/.*[\r\n]*',value='',regex=True)    #Remove URLS
df_Text= df_Text.replace(to_replace=[r'\d+', '$', '@', ',', '/', '&', '#', '!', '_',';', ':','\n', '\t','^A-Za-z0-9','"', '|',' - ', '-'], value='',regex=True)             #No Punctuation ,No Numbers
df_Country= df_Country.replace(to_replace=[r'\d+', '$', '@', ',', '/', '&', '#', '!', '_',';', ':','\n', '\t','^A-Za-z', '"', '|', ' - ', '-'], value='', regex=True)

# print(len(df_Text))
# print(len(df_Country))

#Dataframe to List conversion
filtered_tweets= df_Text.values.tolist()
filtered_country= df_Country.values.tolist()
#print(len(filtered_tweets))

## Clean Tweet Texts
Cleaned_Tweets=[]
def deem1(tweet_text):
    clean_string = tweet_text.encode('ascii', 'ignore').decode('ascii')         #Removes all non-Ascii Characaters
    Cleaned_Tweets.append(clean_string)
for every_tweet in filtered_tweets:
    deem1(every_tweet)

#Cleaned Country Names
Cleaned_Country=[]
def deem2(tweet_country):
    clean_string = tweet_country.encode('ascii', 'ignore').decode('ascii')
    Cleaned_Country.append(clean_string)
for every_country in filtered_country:
    deem2(every_country)   

# print(Cleaned_Tweets)
# print('\n\n')
# print(len(Cleaned_Tweets))
# print('\n\n')
# print(Cleaned_Country)                                 # Getting Full length Tweets

#Sentiment Analysis on Twitter Texts
TB_objects= [TextBlob(part_tweet) for part_tweet in Cleaned_Tweets]
tweet_sentiment = [[object.sentiment.polarity, str(object)] for object in TB_objects]
sentiment_polarity_df= pd.DataFrame(tweet_sentiment, columns=['Sentiment_Polarity', 'Tweet'])

print(sentiment_polarity_df.head(50))

# #Set the Tweet as index (to differentiate between +, - and neutral)
sentiment_polarity_df= sentiment_polarity_df.set_index('Tweet')
#print(sentiment_polarity_df)

#Classification as Positive, Negative and Neutral Tweets
PT_df= sentiment_polarity_df.loc[sentiment_polarity_df['Sentiment_Polarity'] > 0]
NT_df= sentiment_polarity_df.loc[sentiment_polarity_df['Sentiment_Polarity'] < 0]
Neut_df= sentiment_polarity_df.loc[sentiment_polarity_df['Sentiment_Polarity'] == 0]
print(PT_df)
print('\n\n')
print(NT_df)
print('\n\n')
print(Neut_df)

# #Remove Zero Polarity Values Tweets (for Histogram creation)
PN_sentiment_df=sentiment_polarity_df[sentiment_polarity_df.Sentiment_Polarity != 0]

#Reset Index of positive, negative and neutral dataframe
PT_df= PT_df.reset_index()
NT_df= NT_df.reset_index()
Neut_df= Neut_df.reset_index()
PN_sentiment_df= PN_sentiment_df.reset_index()
# print(PT_df)
# print(NT_df)
# print(Neut_df)
# print(PN_sentiment_df)1

## Dictionary conversion for app.py

P_df = PT_df.iloc[:,0]
N_df = NT_df.iloc[:,0]
PT_dict = P_df.to_dict()
print(PT_dict)
NT_dict = N_df.to_dict()
print(NT_dict)

# Pie Plot of Positive, Negative and Neutral Tweets
Area=[len(PT_df), len(NT_df), len(Neut_df)]
boom=(0,0,0.1)
labels='Positive Tweets', 'Negative Tweets', 'Neutral Tweets'
plt.pie(Area, explode=boom,labels= labels, colors=['green', 'red', 'yellow'], autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('Percentage of Tweets Sentiment for %s' %User_word)
plt.show()

#Plot of "Sentiment Polarity vs Number of tweets"
figure, axes= plt.subplots(figsize=(6,6))
PN_sentiment_df.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1], ax=axes, color= ['r'])
#Plot Xlabel ylabel and title
plt.xlabel('More Negative<--------------->More Positive')
plt.ylabel('Number of Tweets on %s' %User_word)
plt.title('People Sentiment on %s (Globally)' %User_word)
#Remove grid and tick labels
plt.grid(b=None)
axes.set_ylabel('Tweets Count')
axes.set_yticklabels([])
plt.yticks([])
#Show plot
plt.show()
# #********************************ADD VISUALIZATIONS********************************************************************


#Convert Positive dataframe to list
PT_list= PT_df['Tweet'].values.tolist()
NT_list= NT_df['Tweet'].values.tolist()
# print(PT_list)
# print(NT_list)


# ##Rake Algorithm
# # r= Rake()
# # Rake_PTlist = [r.extract_keywords_from_text(text) for text in PT_list]
# # print(Rake_PTlist)

# #Performed Tokenization and lowercase all the words to find uniquee words
#Tokenization using split
# PTW_list= [sentence.lower().split() for sentence in PT_list]
# print('By Split:\n', PTW_list)
# NTW_list= [sentence.lower().split() for sentence in NT_list]
# print(NTW_list)
# print('\n\n\n')


#Tokenization using TweetTokenizer()
PTW_list= [TweetTokenizer().tokenize(sentence) for sentence in PT_list]
NTW_list= [TweetTokenizer().tokenize(sentence) for sentence in NT_list]
print(PTW_list)
print('\n\n\n')
print(NTW_list)

# # # #tokenization using Word_Token------------------------------------------>Not good as comapred to tweet tokenizer however tweet tokenizer splits the digit if whole>8/10
# # # # PTW1_list= [nltk.word_tokenize(sentence) for sentence in PT_list]
# # # # NTW1_list= [nltk.word_tokenize(sentence) for sentence in NT_list]
# # # # print(PTW1_list)
# # # # print('\n\n\n\n')
# # # # print(NTW1_list)

#Remove Stopwords using ntlk stopwords and punctuation
Custom_words= set(stopwords.words('english') + list(punctuation))
Custom_words.update(['..','...','....', 'has', 'have', "hasn't", "haven't", 'there', 'their', 'a', 'i', 'the', 'A', 'THE', 'I', 'why', "isn't"
'was', 'then', 'than','im', 'IM', 'many', 'much', 'more'])
PSense_words=[]
for each_sentence_list in PTW_list:
    for each_word in each_sentence_list:
        if each_word not in Custom_words:
            PSense_words.append(each_word)
NSense_words=[]
for every_sentence in NTW_list:
    for every_word in every_sentence:
        if every_word not in Custom_words:
            NSense_words.append(every_word)
# print('No Stopwords, Positive words list:\n', PSense_words)
# print('\n\n')
# print('No Stopwords, Negative words list:\n', NSense_words)

#Lowr case all the letters which will help in finding unique characters 
psense_words= [every_word.lower() for every_word in PSense_words]
nsense_words= [every_word.lower() for every_word in NSense_words]
# print('Lowercase Positive words list:\n', psense_words)
# print('\n\n')
# print('Lowercase Negative words list:\n', nsense_words)


#Remove collection words
Collection_words=[User_word.lower()]            #Lowercasing is already done in above step so whatever is the keyword it will be in list
Nokeyword_Pwordlist=[]
Nokeyword_Nwordlist=[]
for word in psense_words:
    if word not in Collection_words:
        Nokeyword_Pwordlist.append(word)
for w in nsense_words:
    if w not in Collection_words:
        Nokeyword_Nwordlist.append(w)  
# print('Without keyword, Negative word list:\n', Nokeyword_Nwordlist)
# print('\n\n')
# print('Without keyword, Positive word list:\n', Nokeyword_Pwordlist)

# #FOr Bigrams(Co-occurence of words)
# P_Bigrams= nltk.bigrams(Nokeyword_Pwordlist)
# P_Bigrams=list(P_Bigrams)
# #print('Bigram for Positive words:\n', P_Bigrams)
# N_Bigrams= nltk.bigrams(Nokeyword_Nwordlist)
# N_Bigrams=list(N_Bigrams)
# # print('Bigram for Negative words:\n', N_Bigrams)
# # print('\n\n\n\n')
# #Create a counter to find out how many times a word appears-----------> Need later on
# P_common_bigrams=collections.Counter(P_Bigrams)
# Ptop_bigrams= P_common_bigrams.most_common(10)
# #print('Top 10 common Bigrams:\n', Ptop_bigrams)
# N_common_bigrams= collections.Counter(N_Bigrams)  
# Ntop_bigrams= N_common_bigrams.most_common(10)
# #print('Top 10 common neg bigrams:\n', Ntop_bigrams)

# #Create a dataframe of top common bigrams
# Ptop_bg_df= pd.DataFrame(Ptop_bigrams, columns=['Words', 'Count'])
# Pbigrams_df= Ptop_bg_df.iloc[:,0]
# # print('Positive Bigrams Dataframe:\n', Pbigrams_df)
# # print('\n\n\n')
# Ntop_bg_df= pd.DataFrame(Ntop_bigrams, columns=['Words', 'Count'])
# Nbigrams_df= Ntop_bg_df.iloc[:,0]
# # print('\n\n\n')
# # print('Negative Bigrams Datfarme:\n', Nbigrams_df)
# # print('\n\n\n')

# #Creat a list of bigrams
# Pbigrams_list=Pbigrams_df.values.tolist()
# Nbigrams_list=Nbigrams_df.values.tolist()
# # print('Pbigrams list:\n', Pbigrams_list)
# # print('\n\n\n')
# # print('Nbigrams list:\n', Nbigrams_list)

# # ###########################Not Needed####################################
# # # # #  # # # #For Textblob: Using Iterate so as to convert in a dataframe because I'm getting output as [[(1,2)],[(3,4)]] whereas I want [(1,2), (3,4)]
# # # # # Pbigrams_merged_words= list(itertools.chain(*Pbigrams_list))
# # # # # Nbigrams_merged_words= list(itertools.chain(*Nbigrams_list))
# # # # # print('List1:\n', Pbigrams_merged_words)
# # # # # print('\n\n\n')
# # # # # print('List2:\n', Nbigrams_merged_words)

# # # # # nodup_pbigrams = list(set(Pbigrams_merged_words))
# # # # # nodup_nbigrams = list(set(Nbigrams_merged_words))
# # # # # print(nodup_pbigrams)
# # # # # print(nodup_nbigrams)
# # #########################################################################

# # # # #Display a chart of most common words used for the keyword in positive and negative tweets (Remaining)

# #POS Tagging********************Spacy*******************************
# #Method 1: Text Blob------------->Not using
# # PTags=[]
# # for word in Nokeyword_Pwordlist:
# #     Pb= TextBlob(word)
# #     PTags.append(Pb.tags)
# # # print('Ptags are:\n', PTags)
# # # print('\n\n\n\n')
# # NTags=[]
# # for word in Nokeyword_Nwordlist:
# #     Nb= TextBlob(word)
# #     NTags.append(Nb.tags)
# # print('Ntages are:\n', NTags)
# # print('+++++++')

# # # # ##MEthod2: NLTK Pos_tag------------>Not using
# # # # PTags1=[]
# # # # for word in Nokeyword_Pwordlist:
# # # #     b= nltk.pos_tag(word)
# # # #     PTags1.append(b)
# # # # print('Pos_Tag Mthod Results:\n', PTags1)

##Mthod3: Spacy
PTags=[]
nlp = spacy.load("en_core_web_sm")
for pt in Nokeyword_Pwordlist:
    P_tokens = nlp(pt)
    for P_token in P_tokens:
        tabs= (pt, P_token.pos_)
        PTags.append(tabs)
print('Spacy Tag Result of Positive Tweet words:\n', PTags)
#print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
NTags=[]
for nt in Nokeyword_Nwordlist:
    N_tokens = nlp(nt)
    for N_token in N_tokens:
        tabs= (nt, N_token.pos_)
        NTags.append(tabs)
print('Spacy Tag Result of Negative Tweet words:\n', NTags)

# #For Textblob: Using Iterate so as to convert in a dataframe because I'm getting output as [[(1,2)],[(3,4)]] whereas I want [(1,2), (3,4)]
# PMerged_words= list(itertools.chain(*PTags))
# #print(PMerged_words)
# NMerged_words= list(itertools.chain(*NTags))
# #print(NMerged_words)

#Converting Positive and NEgative words with their tags to respective Dataframes
P_Tags_df= pd.DataFrame(PTags, columns=['Pword', 'Tag'])
print('Positive words with tags:\n', P_Tags_df)
print('\n\n')
N_Tags_df= pd.DataFrame(NTags, columns=['Nword', 'Tag'])
print('Negative words with tags:\n', N_Tags_df)

#Set Index as PWord to classify Noun, Adjective and Verb Tags
P_Tags_df= P_Tags_df.set_index('Pword')

Pnoun_Tags_df= P_Tags_df.loc[P_Tags_df['Tag'] == 'NOUN']
Pverb_Tags_df= P_Tags_df.loc[P_Tags_df['Tag'] == 'VERB']
Padj_Tags_df= P_Tags_df.loc[P_Tags_df['Tag'] == 'ADJ']

Pnoun_Tags_df=Pnoun_Tags_df.reset_index()
Pverb_Tags_df=Pverb_Tags_df.reset_index()
Padj_Tags_df=Padj_Tags_df.reset_index()

Pnoun_words_df= Pnoun_Tags_df.iloc[:,0]
Pverb_words_df= Pverb_Tags_df.iloc[:,0]
Padj_words_df= Padj_Tags_df.iloc[:,0]

Pnoun_list= Pnoun_words_df.values.tolist()
Pverb_list= Pverb_words_df.values.tolist()
Padj_list= Padj_words_df.values.tolist()
# print(Pnoun_list)
# print(Pverb_list)
# print(Padj_list)

##Set Index as NWord to classify Noun, Adjective and Verb Tags
N_Tags_df= N_Tags_df.set_index('Nword')

Nnoun_Tags_df= N_Tags_df.loc[N_Tags_df['Tag'] == 'NOUN']
Nverb_Tags_df= N_Tags_df.loc[N_Tags_df['Tag'] == 'VERB']
Nadj_Tags_df= N_Tags_df.loc[N_Tags_df['Tag'] == 'ADJ']

Nnoun_Tags_df=Nnoun_Tags_df.reset_index()
Nverb_Tags_df=Nverb_Tags_df.reset_index()
Nadj_Tags_df=Nadj_Tags_df.reset_index()

Nnoun_words_df= Nnoun_Tags_df.iloc[:,0]
Nverb_words_df= Nverb_Tags_df.iloc[:,0]
Nadj_words_df= Nadj_Tags_df.iloc[:,0]

Nnoun_list= Nnoun_words_df.values.tolist()
Nverb_list= Nverb_words_df.values.tolist()
Nadj_list= Nadj_words_df.values.tolist()
# print('Noun:\n', Nnoun_list)
# print('Verb:\n', Nverb_list)
# print('Adj:\n', Nadj_list)

#Lemmatizer for Postive POS words
lemm = WordNetLemmatizer()
P_lemm_nwords = [lemm.lemmatize(n, pos='n') for n in Pnoun_list]
P_lemm_vwords = [lemm.lemmatize(v , pos='v') for v in Pverb_list]
P_lemm_awords = [lemm.lemmatize(a , pos='a') for a in Padj_list]



#Lemmatizer for Negative POS words
N_lemm_nwords = [lemm.lemmatize(N , pos='n') for N in Nnoun_list]
N_lemm_vwords = [lemm.lemmatize(V , pos='v') for V in Nverb_list]
N_lemm_awords = [lemm.lemmatize(A , pos='a') for A in Nadj_list]

# # print('PLemm Noun:\n', P_lemm_nwords)
# # print('NLemm Noun:\n', N_lemm_nwords)
# # print('PLemm verb:\n', P_lemm_vwords)
# # print('NLemm verb:\n', N_lemm_vwords)
# # print('PLemm Adj:\n', P_lemm_awords)
# # print('NLemm Adj:\n', N_lemm_awords)

# # # # print('\n\n\n')

#Duplicate removals
Nouns_pos_tweet= list(set(P_lemm_nwords))
Verbs_pos_tweet= list(set(P_lemm_vwords))
Adj_pos_tweet= list(set(P_lemm_awords))
Nouns_neg_tweet= list(set(N_lemm_nwords))
Verbs_neg_tweet= list(set(N_lemm_vwords))
Adj_neg_tweet= list(set(N_lemm_awords))

print('Nouns from Positive Tweets:\n', Nouns_pos_tweet)
print('Nouns from Negative Tweets:\n', Nouns_neg_tweet)
print('Verbs from Positive Tweets:\n', Verbs_pos_tweet)
print('Verbs from Negative Tweets:\n', Verbs_neg_tweet)
print('Adjectives from Positive Tweets:\n', Adj_pos_tweet)
print('Adjectives from Positive Tweets:\n', Adj_neg_tweet)

# Prepare a counter for common words in positive tweets
counts_posnoun_words=collections.Counter(P_lemm_nwords)
PC_noun_words= counts_posnoun_words.most_common(10)

counts_posverb_words=collections.Counter(P_lemm_vwords)
PC_verb_words= counts_posverb_words.most_common(10)

counts_posadj_words=collections.Counter(P_lemm_awords)
PC_adj_words= counts_posadj_words.most_common(10)

# # print('Common Noun Words from Positive Tweets:\n', PC_noun_words)
# # print('\n\n')
# # print('Common Verb Words from Positive Tweets:\n', PC_verb_words)
# # print('\n\n')
# # print('Common Adjective Words from Positive Tweets:\n', PC_adj_words)
# # print('\n\n')

#Prepare a counter for common words in negative tweets
counts_negnoun_words=collections.Counter(N_lemm_nwords)
NC_noun_words= counts_negnoun_words.most_common(10)

counts_negverb_words=collections.Counter(N_lemm_vwords)
NC_verb_words= counts_negverb_words.most_common(10)

counts_negadj_words=collections.Counter(N_lemm_awords)
NC_adj_words= counts_negadj_words.most_common(10)

# # print('Common Noun Words from Negative Tweets:\n', NC_noun_words)
# # print('\n\n') 
# # print('Common Verb Words from Negative Tweets:\n', NC_verb_words)
# # print('\n\n')
# # print('Common Adjective Words from Negative Tweets:\n', NC_adj_words)

#Join all the list of common nouns, verbs, adjectives
Joined_list = [*PC_noun_words, *NC_noun_words, *PC_verb_words, *NC_verb_words, *PC_adj_words, *NC_adj_words]
print(Joined_list)
#Joined_list = [*PC_noun_words, *NC_noun_words, *PC_adj_words, *NC_adj_words]

# # J_lemm_words = [lemm.lemmatize(item, pos=) for item in Joined_list]
# # J_unique = list(set(J_lemm_words))
# # print(J_unique)

Joined_df= pd.DataFrame(Joined_list, columns=['Common Words', 'count'])
# #print(Joined_df)
Word_Cloud_df= Joined_df.iloc[:,0]
# #print(Word_Cloud_df)

WC_dict = Word_Cloud_df.to_dict()
print(WC_dict)

#Creating a list of Word clouds from dataframe to remove count numbers
Word_Cloud_list= Word_Cloud_df.values.tolist()
# print('\n\n\n')
print('Word CLoud List:\n', Word_Cloud_list)

# # # # Remove userwor-------->NAAHHH
# # # # WCL=[] 
# # # # for word in Word_Cloud_list:
# # # #     pattern=User_word
# # # #     unique_words = re.match(r'pattern','', word)
# # # #     WCL.append(unique_words)

# # # # print('WCL:\n', WCL)

##Duplicate removals
Word_Cloud_list= list(set(Word_Cloud_list))

#Converting list to string as Word Cloud takes only String into consideration
Word_Cloud_String = ','.join(Word_Cloud_list)
print(Word_Cloud_String)

# # # # # # # # #Spelling correct using textblob                                  ##Spellin gchecker cannot be used(Ex: Avengers: Avenues)
# # # # # # # # WC_correct_string = TextBlob(Word_Cloud_String).correct()
# # # # # # # # print('Corrected String:\n', WC_correct_string)


# # Thumbsup Image
# # mask = np.array(Image.open('tr2.png'))
# # mask.shape

# # image_color = ImageColorGenerator(mask)
#Creating Word Cloud    
sw = set(STOPWORDS)
wordcloud = WordCloud(width=1600, height=900, stopwords=sw, min_font_size=25).generate(Word_Cloud_String)
plt.figure(figsize=(12,12), facecolor= 'k')
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()






    





    
    



