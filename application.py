import tweepy
import wikipedia
#import time
import random
import sys
from os import environ


consumer_key = environ['API_KEY']
consumer_secret_key = environ['API_SECRET_KEY']
access_token = environ['ACCESS_TOKEN']
access_token_secret = environ['ACCESS_TOKEN_SECRET']

pages = ["Wang Yibo", "Xiao Zhan"]

def get_quote():
    term = random.choice(pages)
    res = wikipedia.page(term)
    page = res.content
    length = len(page)
    low = random.randint(0, length)
    high = random.randint(0, length)
    if low > high:
        tmp = high
        high = low
        low = tmp
    if high - low > 280:
        high = low + 280
    
    return page[low:high]


def tweet_quote(): 
    #interval = 60 * 60

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweet = get_quote()
    api.update_status(tweet)
    

    # while True:
    #     tweet = get_quote()
    #     api.update_status(tweet)
    #     time.sleep(interval)
    


if __name__ == "__main__":
    tweet_quote()