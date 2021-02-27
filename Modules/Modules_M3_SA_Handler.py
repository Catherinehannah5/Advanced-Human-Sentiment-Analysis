import pandas as pd
from textblob import TextBlob
import time

## Timer
start = time.time()

def Sentiment_Analyzer(Cleaned_Tweets):
    #Sentiment Analysis on Twitter Texts
    TB_objects= [TextBlob(part_tweet) for part_tweet in Cleaned_Tweets]
    tweet_sentiment = [[object.sentiment.polarity, str(object)] for object in TB_objects]
    sentiment_polarity_df= pd.DataFrame(tweet_sentiment, columns=['Sentiment_Polarity', 'Tweet'])

    ## Set the Tweet as index (to differentiate between +, - and neutral)
    sentiment_polarity_df= sentiment_polarity_df.set_index('Tweet')
    Total = sentiment_polarity_df.iloc[:,0]
    Total = len(Total)
    #print('Total tweets: ', Total)

    ## Classification as Positive, Negative and Neutral Tweets
    PT_df= sentiment_polarity_df.loc[sentiment_polarity_df['Sentiment_Polarity'] > 0]
    NT_df= sentiment_polarity_df.loc[sentiment_polarity_df['Sentiment_Polarity'] < 0]
    Neut_df= sentiment_polarity_df.loc[sentiment_polarity_df['Sentiment_Polarity'] == 0]

    Highly_PT_df= sentiment_polarity_df.loc[sentiment_polarity_df['Sentiment_Polarity'] > 0.5]
    Slightly_PT_df = sentiment_polarity_df.loc[(sentiment_polarity_df['Sentiment_Polarity'] > 0) & (sentiment_polarity_df['Sentiment_Polarity'] <= 0.5)]
    Highly_NT_df= sentiment_polarity_df.loc[sentiment_polarity_df['Sentiment_Polarity'] < -0.5]
    Slightly_NT_df = sentiment_polarity_df.loc[(sentiment_polarity_df['Sentiment_Polarity'] >= -0.5) & (sentiment_polarity_df['Sentiment_Polarity'] < 0)]
    Neut_df= sentiment_polarity_df.loc[sentiment_polarity_df['Sentiment_Polarity'] == 0]
    
    # #Remove Zero Polarity Values Tweets (for Histogram creation)
    PN_sentiment_df=sentiment_polarity_df[sentiment_polarity_df.Sentiment_Polarity != 0]

    ## Reset Index
    PT_df= PT_df.reset_index()
    NT_df= NT_df.reset_index()
    Highly_PT_df= Highly_PT_df.reset_index()
    Slightly_PT_df= Slightly_PT_df.reset_index()
    Highly_NT_df= Highly_NT_df.reset_index()
    Slightly_NT_df= Slightly_NT_df.reset_index()
    Neut_df= Neut_df.reset_index()
    PN_sentiment_df= PN_sentiment_df.reset_index()

    ## Division
    Highly_PT_df = Highly_PT_df.iloc[:,0]
    Highly_PT_df = len(Highly_PT_df)
    H_percentage = (Highly_PT_df*100)/Total
    #print(H_percentage)

    Slightly_PT_df = Slightly_PT_df.iloc[:,0]
    Slightly_PT_df = len(Slightly_PT_df)
    SP_percentage = (Slightly_PT_df*100)/Total
    #print(SP_percentage)

    Highly_NT_df = Highly_NT_df.iloc[:,0]
    Highly_NT_df = len(Highly_NT_df)
    N_percentage = (Highly_NT_df*100)/Total
    #print(N_percentage)

    Slightly_NT_df = Slightly_NT_df.iloc[:,0]
    Slightly_NT_df = len(Slightly_NT_df)
    SN_percentage = (Slightly_NT_df*100)/Total
    #print(SN_percentage)

    Neut_df = Neut_df.iloc[:,0]
    Neut_df = len(Neut_df)
    Neut_percentage = (Neut_df*100)/Total
    #print(Neut_percentage)

    Name = ['Highly_PT_df', H_percentage, 'Slightly_PT_df', SP_percentage, 'Highly_NT_df', N_percentage, 'Slightly_NT_df', SN_percentage, 'Neut_df', Neut_percentage]
    
    W = iter(Name)
    Pie_dict = dict(zip(W,W))

    PT_list= PT_df['Tweet'].values.tolist()
    NT_list= NT_df['Tweet'].values.tolist()
    
    PT_values= PT_df['Sentiment_Polarity'].values.tolist()
    NT_values= NT_df['Sentiment_Polarity'].values.tolist()
    #Zero_values = Neut_df['Sentiment_Polarity'].values.tolist()

    return PT_list, NT_list, PT_df, NT_df, Neut_df, Pie_dict, PT_values, NT_values

end =(start - time.time())
#print('Time Taken By M3: ', end)