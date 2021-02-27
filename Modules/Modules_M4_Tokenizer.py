import pandas as pd
from nltk.tokenize import TweetTokenizer
from multiprocessing import Process
from nltk.corpus import stopwords
from string import punctuation
import collections
import time

## Time Clock
start = time.time()

Custom_words= set(stopwords.words('english') + list(punctuation))
Custom_words.update(['..','...','....', 'has', 'have', "hasn't", "haven't", 'there', 'their', 'a', 'i', 'the', 'A', 'THE', 'I', 'why', "isn't"
'was', 'then', 'than','im', 'IM', 'many', 'much', 'more'])

def Pos_Tokenizer(PT_list, User_word):

    #Tokenization using TweetTokenizer()
    PTW_list= [TweetTokenizer().tokenize(sentence) for sentence in PT_list]

    #Remove Stopwords using ntlk stopwords and punctuation
    PSense_words=[]
    for each_sentence_list in PTW_list:
        for each_word in each_sentence_list:
            if each_word not in Custom_words:
                PSense_words.append(each_word)

    #Lowr case all the letters which will help in finding unique characters
    psense_words= [every_word.lower() for every_word in PSense_words]

    #Remove collection words
    Nokeyword_Pwordlist=[]
    for word in psense_words:
        if word not in User_word.lower():
            Nokeyword_Pwordlist.append(word)

    return Nokeyword_Pwordlist  

def Neg_Tokenizer(NT_list, User_word):

    #Tokenization using TweetTokenizer()
    NTW_list= [TweetTokenizer().tokenize(sentence) for sentence in NT_list]
    
    #Remove Stopwords using ntlk stopwords and punctuation
    NSense_words=[]
    for every_sentence in NTW_list:
        for every_word in every_sentence:
            if every_word not in Custom_words:
                NSense_words.append(every_word)

    #Lowr case all the letters which will help in finding unique characters
    nsense_words= [every_word.lower() for every_word in NSense_words]

    #Remove collection words
    Nokeyword_Nwordlist=[]
    for w in nsense_words:
        if w not in User_word.lower():
            Nokeyword_Nwordlist.append(w)

    return Nokeyword_Nwordlist             

end = (start - time.time())
#print('Time Taken By M4: ', end)