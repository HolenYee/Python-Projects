import tweepy
import time

consumer_key = "VJuYBEB9R9pNLjbYsrujbfBw4"
consumer_secret = "REszrc9Zv5dGLffvc8zsxNW19FDxO3JjHQKvmS512cE7Ntr4ZG"
key = "1338145117761400840-ARToRI4ioQ1dd71teHvD3Zc8cdbIYY"
secret = "RAAXF7LOE46zLnJArFAmRXHxX7wIfU7TqKJnlYToFKesJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = "#theaveragejoe"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).pages(tweetNumber)

def retweetbot():
    for tweet in tweets:
        try:
            api.retweet(tweet[0].id)
            print("Retweet done")
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(5)

retweetbot()
