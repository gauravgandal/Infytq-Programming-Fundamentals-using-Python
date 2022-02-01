import tweepy
consumer_key= '46Z7m1x06up4eP9KsOE0slu2S'
consumer_secret= 'XyYYfobEVDfXeXc1TG37V2ZFBi9KGfXy5EqtwZ59N5jo9ZOzGq'
access_token= '1473611034623578112-GSS4xCHxWVVpraDDsOMBkhaKcrMQmp'
access_token_secret= 'K17MxznlXDw2agCkOdNNF0AhutVjNfqGbEikJxr6ZK3zZ'

client = tweepy.Client(consumer_key= consumer_key,consumer_secret= consumer_secret,access_token= access_token,access_token_secret= access_token_secret)
query = 'news'
tweets = client.search_recent_tweets(query=query, max_results=10)
for tweet in tweets.data:
    print(tweet.text)