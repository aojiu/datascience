import tweepy
import textblob

cosumer_key = "K7s0RNIAlAGNgKOAkkniXMCJ8"
consumer_sec = "ee82MGBbeaJMZmzp7oAwuHDEmQjbFp4b33UE4EW4UiF7CRxsWS"

access_key = "879872311653957633-KN56c9Nk71dHMaKwjjAulQxf2cJVun1"
access_secret = "iq13PxEzKzSwqFVUXqgxTwqpVDRr8s6NZgql8ixh8dPIT"

auth = tweepy.OAuthHandler(consumer_sec, consumer_sec)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

public_tweets = api.search("Nintendo")

for tweet in public_tweets:
    print(tweet.text)
    analysis = textblob(tweet.text)
    print(analysis.sentiment)
