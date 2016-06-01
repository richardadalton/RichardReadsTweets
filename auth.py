
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = '<Consumer Key>'
CONSUMER_SECRET = '<Consumer Secret>'
OAUTH_TOKEN = '<OAuth Token>'
OAUTH_TOKEN_SECRET = '<OAuth Token Secret>'

def get_auth():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return auth

def get_api():
    auth = get_auth()
    return tweepy.API(auth)
