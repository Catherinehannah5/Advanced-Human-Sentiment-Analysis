from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

def Pie_Plot(PT_df, NT_df, Neut_df, User_word):
    # Pie Plot of Positive, Negative and Neutral Tweets
    Area=[len(PT_df), len(NT_df), len(Neut_df)]
    boom=(0,0,0.1)
    labels='Positive Tweets', 'Negative Tweets', 'Neutral Tweets'
    plt.pie(Area, explode=boom,labels= labels, colors=['green', 'red', 'yellow'], autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title('Percentage of Tweets Sentiment for %s' %User_word)
    plt.show()


def Word_Cloud(Word_Cloud_String):
    #Creating Word Cloud    
    sw = set(STOPWORDS)
    wordcloud = WordCloud(width=1600, height=900, stopwords=sw, min_font_size=25).generate(Word_Cloud_String)
    plt.figure(figsize=(12,12), facecolor= 'k')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
