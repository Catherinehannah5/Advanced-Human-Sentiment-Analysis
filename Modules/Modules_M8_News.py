import requests
from bs4 import BeautifulSoup 
import json
import pandas as pd
import time

## Timer
start = time.time()

def News():
    url = 'https://inshorts.com/en/read'    #Fetching from Inshorts Website
    response = requests.get(url)

    #print(response)
    Recent_News=[]
    soup = BeautifulSoup(response.text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    for headline in headlines:
        News = headline.text
        Recent_News.append(News)
    
    return Recent_News

News()

end = start - time.time()
#print('Time Taken By M8: ', end)