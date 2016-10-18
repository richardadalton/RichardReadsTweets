import tweepy
from auth import get_api

api = get_api()


def search(query, count):
    return [status for status in tweepy.Cursor(api.search, q=query).items(count)]

