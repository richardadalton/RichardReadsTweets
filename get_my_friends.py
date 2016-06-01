import tweepy
from auth import get_api

api = get_api()

def get_friends_of(username):
    user = api.get_user(username)
    return user.friends()


for friend in get_friends_of("@richardadalton"):
    print friend
