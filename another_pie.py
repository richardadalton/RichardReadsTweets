import json
import pandas as panda
import matplotlib.pyplot as plt
import re

tweets_data_path = 'tweet_mining.json'

def read_json(file_path):
    results = []

    tweets_file = open(file_path, "r")

    for tweet_line in tweets_file:
        try:
            status = json.loads(tweet_line)
            results.append(status)
        except:
            continue

    return results

def is_token_in_tweet_text(token, tweet_text):
    token = token.lower()
    tweet_text = tweet_text.lower()
    match = re.search(token, tweet_text)
    if match:
        return True
    return False


def reshape_data(results):
    statuses = panda.DataFrame()

    statuses['text'] = map(lambda s: s['text'], results)
    statuses['lang'] = map(lambda s: s['lang'], results)
    statuses['country'] = map(lambda s: s['place']['country']
                                if s['place'] != None else None, results)

    statuses['python'] = statuses['text'].apply(lambda s: is_token_in_tweet_text('python', s))
    statuses['java'] = statuses['text'].apply(lambda s: is_token_in_tweet_text('java', s))
    statuses['c#'] = statuses['text'].apply(lambda s: is_token_in_tweet_text('c#', s))
    statuses['f#'] = statuses['text'].apply(lambda s: is_token_in_tweet_text('f#', s))
    return statuses


results = read_json(tweets_data_path)
statuses = reshape_data(results)


labels = ['python', 'java', 'c#', 'f#']

slices = [
    statuses['python'].value_counts()[True],
    statuses['java'].value_counts()[True],
    statuses['c#'].value_counts()[True],
    statuses['f#'].value_counts()[True]
]

slices = map(lambda k: statuses[k].value_counts()[True], labels)

slices = [statuses[k].value_counts()[True] for k in labels]

plt.pie(slices, labels=labels)
plt.show()