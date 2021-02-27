import pandas as pd
from nltk.stem.wordnet import WordNetLemmatizer
import collections
import time

## Timer
start = time.time()

def Pos_lemm(Pnoun_list, Pverb_list, Padj_list):

    lemm = WordNetLemmatizer()

    ## Lemmatizer for Positive POS words
    P_lemm_nwords = [lemm.lemmatize(n, pos='n') for n in Pnoun_list]
    P_lemm_vwords = [lemm.lemmatize(v , pos='v') for v in Pverb_list]
    P_lemm_awords = [lemm.lemmatize(a , pos='a') for a in Padj_list]

    #Duplicate removals
    Nouns_pos_tweet= list(set(P_lemm_nwords))
    Verbs_pos_tweet= list(set(P_lemm_vwords))
    Adj_pos_tweet= list(set(P_lemm_awords))

    ## Prepare a counter for common (Noun, Verb, Adjective) words in positive tweets
    counts_posnoun_words=collections.Counter(Nouns_pos_tweet)
    PC_noun_words= counts_posnoun_words.most_common(10)

    counts_posverb_words=collections.Counter(Verbs_pos_tweet)
    PC_verb_words= counts_posverb_words.most_common(10)

    counts_posadj_words=collections.Counter(Adj_pos_tweet)
    PC_adj_words= counts_posadj_words.most_common(10)

    return PC_noun_words, PC_verb_words, PC_adj_words

def Neg_lemm(Nnoun_list, Nverb_list, Nadj_list):
    lemm = WordNetLemmatizer()

    ## Lemmatizer for Negative POS words
    N_lemm_nwords = [lemm.lemmatize(N , pos='n') for N in Nnoun_list]
    N_lemm_vwords = [lemm.lemmatize(V , pos='v') for V in Nverb_list]
    N_lemm_awords = [lemm.lemmatize(A , pos='a') for A in Nadj_list]

    ## Duplicate removals
    Nouns_neg_tweet= list(set(N_lemm_nwords))
    Verbs_neg_tweet= list(set(N_lemm_vwords))
    Adj_neg_tweet= list(set(N_lemm_awords))

    ## Prepare a counter for common (Noun, Verb, Adjective) words in negative tweets
    counts_negnoun_words=collections.Counter(Nouns_neg_tweet)
    NC_noun_words= counts_negnoun_words.most_common(10)

    counts_negverb_words=collections.Counter(Verbs_neg_tweet)
    NC_verb_words= counts_negverb_words.most_common(10)

    counts_negadj_words=collections.Counter(Adj_neg_tweet)
    NC_adj_words= counts_negadj_words.most_common(10)

    return NC_noun_words, NC_verb_words, NC_adj_words


def Wordlist(PC_noun_words, NC_noun_words, PC_verb_words, NC_verb_words, PC_adj_words, NC_adj_words):

    ## Join all the list of common nouns, verbs, adjectives
    Joined_list = [*PC_noun_words, *NC_noun_words, *PC_verb_words, *NC_verb_words, *PC_adj_words, *NC_adj_words]
    Joined_df= pd.DataFrame(Joined_list, columns=['Common Words', 'count'])
    Word_Cloud_df= Joined_df.iloc[:,0]

    ## Creating a list of Word clouds from dataframe to remove count numbers
    Word_Cloud_list= Word_Cloud_df.values.tolist()

    ## Duplicate removals
    Word_Cloud_list= list(set(Word_Cloud_list))
    WC_dict = Word_Cloud_df.to_dict()

    return WC_dict

end = (start - time.time())
#print('Time Taken By M6: ', end)