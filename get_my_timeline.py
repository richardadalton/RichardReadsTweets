import tweepy
from auth import get_api

api = get_api()


def get_my_timeline(count):
    return tweepy.Cursor(api.home_timeline).items(count)


for status in get_my_timeline(10):
    print status
