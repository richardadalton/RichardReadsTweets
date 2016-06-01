from operator import itemgetter


def most_retweeted(tweets, min_retweets):
    pop_tweets = [status
                  for status in tweets
                  if status._json['retweet_count'] > min_retweets]

    tweets_tup = tuple([(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count'])
                        for tweet in pop_tweets])

    pop_tweets_set = set(tweets_tup)

    return sorted(pop_tweets_set, key=itemgetter(1), reverse=True)[:5]
