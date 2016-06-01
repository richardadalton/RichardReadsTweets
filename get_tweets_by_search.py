import tweepy
from prettytable import PrettyTable
from operator import itemgetter
from auth import get_api

api = get_api()


def search(query, count):
    return [status for status in tweepy.Cursor(api.search, q=query).items(count)]


results = search('Ireland OR Australia', 100)

for tweet in results:
    print tweet
