import nltk

nltk.data.path.append('C:\\Users\\ashik\\nltk_data')

nltk.download('punkt')

from textblob import TextBlob

with open('senti.txt','r')as f:
    text = f.read()


blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)