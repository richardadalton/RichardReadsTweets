from operator import itemgetter
from get_tweets_by_search import search
from get_in_table import make_table

def most_retweeted(tweets, min_retweets):
    pop_tweets = [status
                  for status in tweets
                  if status._json['retweet_count'] > min_retweets]

    # pop_tweets_dict = { tweet._json['text'].encode('utf-8'): tweet._json['retweet_count'] for tweet in pop_tweets}
    #
    # return sorted(pop_tweets_dict, key=itemgetter(1), reverse=True)[:5]



    tweets_tup = tuple([(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count'])
                        for tweet in pop_tweets])

    pop_tweets_set = set(tweets_tup)

    return sorted(pop_tweets_set, key=itemgetter(1), reverse=True)[:5]

tweets = search('Dublin', 150)

pop = most_retweeted(tweets, 10)
print make_table(pop)