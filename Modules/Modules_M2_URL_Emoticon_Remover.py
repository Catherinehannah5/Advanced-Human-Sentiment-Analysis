import pandas as pd
import re
import time

## Timer
start = time.time()

def URL_Emoticon_Cleaner(Tweets_list):
    df_Text=pd.DataFrame({'Text': Tweets_list})
    df_Text= df_Text.replace(to_replace=r'https?:\/\/.*[\r\n]*',value='',regex=True)    #Remove URLS
    df_Text= df_Text.replace(to_replace=[r'\d+', '$', '@', ',', '/', '&', '#', '!', '_',';', ':','\n', '\t','^A-Za-z0-9','"', '|',' - ', '-'], value='',regex=True)
   
    #Dataframe to List conversion
    filtered_tweets= df_Text.values.tolist()

    i=0
    CT = [tweet[i].encode('ascii', 'ignore').decode('ascii') for tweet in filtered_tweets]
    #print('Cleaned Tweets:\n', CT)

    return CT

end = (start - time.time())
#print('Time Taken By M2: ', end)