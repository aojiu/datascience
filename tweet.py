import tweepy
import textblob

cosumer_key = "PvmjejUXuDBGuzdVxqwsw3Q3R"
consumer_sec = "DwGsrHBIB4uIG0MPeUZdOfZ8DYRxczHRgQplqeP58OrQQ3tBvF"

access_key = "879872311653957633-qZKhfCJKiZn4AaMpSjQPEZXr8Pp2hbM"
access_secret = "hsVnFq4PFE51CGp3kTgJUdxm05CqEMOtQjYoxRiIMsPMq"

auth = tweepy.OAuthHandler(cosumer_key, consumer_sec)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

public_tweets = api.search("Nintendo")

for tweet in public_tweets:
    print(tweet.text)
    # analysis = textblob(tweet.text)
    # print(analysis.sentiment)
