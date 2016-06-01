import tweepy
from collections import Counter
from prettytable import PrettyTable
from auth import get_api
from get_tweets_by_search import search

api = get_api()



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




def table_stuff(status_texts, screen_names, words):
    for label, data in (('Text', status_texts), ('Screen Name', screen_names), ('Word', words)):
        table = PrettyTable(field_names=[label, 'Count'])
        counter = Counter(data)

        [table.add_row(entry) for entry in counter.most_common()[:10]]
        table.align[label], table.align['Count'] = 'l', 'r'

        print table


def get_lexical_diversity(items):
    return 1.0 * len(set(items)) / len(items)


def get_average_words(tweets):
    total_words = sum([len(tweet.split()) for tweet in tweets])
    return 1.0 * total_words / len(tweets)


tweets = search('Dublin', 100)
texts = get_tweet_texts(tweets)
words = get_words(texts)
screen_names = get_screen_names(tweets)
hashtags = get_hashtags(tweets)

# print "Averate words: %s" % get_average_words(texts)
# print "Word Diversity: %s" % get_lexical_diversity(words)
# print "Screen Name Diversity: %s" % get_lexical_diversity(screen_names)
# print "HashTag Diversity: %s" % get_lexical_diversity(hashtags)

table_stuff(texts, screen_names, hashtags)

