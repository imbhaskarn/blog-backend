import tweepy
from core.settings import (
    consumer_key,
    consumer_key_secret,
    access_token,
    access_token_secret,
)

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_key_secret, access_token, access_token_secret
)

bot_api = tweepy.API(auth)

data = bot_api.mentions_timeline()
