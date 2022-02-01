from textblob import TextBlob
 
 
def sentiment(polarity):
    if blob.sentiment.polarity < 0:
        print("Negative")
    elif blob.sentiment.polarity > 0:
        print("Positive")
    else:
        print("Neutral")
 
 
blob = TextBlob("The movie was excellent!")
print(blob.sentiment)
sentiment(blob.sentiment.polarity)
 
blob = TextBlob("The movie was not bad.")
print(blob.sentiment)
sentiment(blob.sentiment.polarity)
 
blob = TextBlob("The movie was ridiculous.")
print(blob.sentiment)
sentiment(blob.sentiment.polarity)
