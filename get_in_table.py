from prettytable import PrettyTable
import get_tweets_by_search
import get_most_retweeted

def make_table(tweets):
    table = PrettyTable(field_names=['Text', 'Retweet Count'])
    for key, val in tweets:
        table.add_row([key, val])
        table.max_width['Text'] = 50
        table.align['Text'], table.align['Retweet Count'] = 'l', 'r'
    return table



tweets = get_tweets_by_search.search('Euro', 10)
popular = get_most_retweeted.most_retweeted(tweets, 1000)
print make_table(popular)