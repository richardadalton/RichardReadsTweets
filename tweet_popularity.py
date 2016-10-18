import tweepy
from tweepy import OAuthHandler
from auth import get_api

api = get_api()

count = 150
query = 'Ireland'



def get_tweet_texts(tweets):
    return [status._json['text'].encode('utf-8') for status in tweets]


def get_screen_names(tweets):
    return [status._json['user']['screen_name'].encode('utf-8')
                for status in tweets
                for mention in status._json['entities']['user_mentions']]


def get_words(tweet_texts):
    return [word
        for tweet_text in tweet_texts
        for word in tweet_text.split()]

def get_hashtags(tweets):
    return [hashtag['text'].encode('utf-8')
        for status in tweets
        for hashtag in
        status._json['entities']['hashtags']]


def get_lexical_diversity(items):
    return 1.0 * len(set(items)) / len(items)


def get_average_words(tweets):
    total_words = sum([len(tweet.split()) for tweet in tweets])
    return 1.0 * total_words / len(tweets)



tweets = [status for status in tweepy.Cursor(api.search,  q=query).items(count)]


texts = get_tweet_texts(tweets)
words = get_words(texts)
screen_names = get_screen_names(tweets)
hashtags = get_hashtags(tweets)


print "Averate words: %s" % get_average_words(texts)
print "Word Diversity: %s" % get_lexical_diversity(words)
print "Screen Name Diversity: %s" % get_lexical_diversity(screen_names)
print "HashTag Diversity: %s" % get_lexical_diversity(hashtags)
