# from textblob import TextBlob
# data = "Gaurav is a Good Boy"
# blob= TextBlob(data)
# print(blob)
# print(blob.sentiment.polarity)
'''
API KEY ---> 46Z7m1x06up4eP9KsOE0slu2S
API KEY SECRET ---> XyYYfobEVDfXeXc1TG37V2ZFBi9KGfXy5EqtwZ59N5jo9ZOzGq
BEARERE KEY ---> AAAAAAAAAAAAAAAAAAAAAH03XQEAAAAA8YMfXKKYJq4s20kaMnvdX3wS5mI%3DLv1yBxoECE5Killxf7J6GSZoON4CtqHItYM8wGoPsFZd2ozXsd
Access Token --> 1473611034623578112-GSS4xCHxWVVpraDDsOMBkhaKcrMQmp
Access Token Secret ----> K17MxznlXDw2agCkOdNNF0AhutVjNfqGbEikJxr6ZK3zZ
'''

import tweepy


consumer_key = "46Z7m1x06up4eP9KsOE0slu2S"
consumer_secret = "XyYYfobEVDfXeXc1TG37V2ZFBi9KGfXy5EqtwZ59N5jo9ZOzGq"
key = "1473611034623578112-GSS4xCHxWVVpraDDsOMBkhaKcrMQmp"
secret = "K17MxznlXDw2agCkOdNNF0AhutVjNfqGbEikJxr6ZK3zZ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
search_term = input("Enter the keyword : ")

no_of_search_term = int(input("Enter the number of records to be fetched : "))

tweets = tweepy.Cursor(api.search_tweets,q=search_term,lang="en").items(no_of_search_term)
#print(data)

#api = tweepy.API(auth)
#print(dir(data))
# for tweets in api.search_tweets(q="iphone", lang="en"):
#     print(tweets.text)

for tweet in tweets:
    print(tweet.text)