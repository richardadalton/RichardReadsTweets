import json
import pandas as panda
import re
import matplotlib.pyplot as plt

tweets_data_path = 'tweet_mining.json'

results = []

tweets_file = open(tweets_data_path, "r")
for tweet_line in tweets_file:
    try:
        status = json.loads(tweet_line)
        results.append(status)
    except:
        continue

print len(results)


#create  a dataframe
statuses = panda.DataFrame()

# store the text values
statuses['text'] = map(lambda status: status['text'], results)
#store the languge values
statuses['lang'] = map(lambda status: status['lang'], results)
#sometines there may not be a 'place' listed in the tweet , so set to 'None' if not present
statuses['country'] = map(lambda status: status['place']['country'] if status['place'] != None else None, results)

#get each tweet language and the  count of its appearance (not to be confused with programming languages)
tweets_by_lang = statuses['lang'].value_counts()



# create our drawing space/window (figure)
fig = plt.figure()

# add a plot area for our data on the figure - 1,1,1 means a single chart/graph
ax = fig.add_subplot(1,1,1)

#style the axes and labels of our plot
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Tweet Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.xaxis.label.set_color('#666666')
ax.yaxis.label.set_color('#666666')
ax.tick_params(axis='x', colors='#666666')
ax.tick_params(axis='y', colors='#666666')
#style the title
ax.set_title('Top 10 languages', fontsize=15, color='#666666')

#plot the top 10 tweet languages and appearance count using a bar chart
tweets_by_lang[:10].plot(ax=ax, kind='bar', color='#FF7A00')

#color the spines (borders)
for spine in ax.spines.values():
        spine.set_edgecolor('#666666')

# render the graph
plt.show()






#
#
#
#
#
#
#
#
# def read_json(file_path):
#     results = []
#
#     tweets_file = open(file_path, "r")
#
#     for tweet_line in tweets_file:
#         try:
#             status = json.loads(tweet_line)
#             results.append(status)
#         except:
#             continue
#
#     return results
#
# def is_token_in_tweet_text(token, tweet_text):
#     token = token.lower()
#     tweet_text = tweet_text.lower()
#     match = re.search(token, tweet_text)
#     if match:
#         return True
#     return False
#
#
# def is_python_in_tweet(text):
#     return is_token_in_tweet_text("python", text)
#
#
# results = read_json(tweets_data_path)
#
# statuses = panda.DataFrame()
#
# statuses['text'] = map(lambda s: s['text'], results)
# statuses['lang'] = map(lambda s: s['lang'], results)
# statuses['country'] = map(lambda s: s['place']['country']
#                             if s['place'] is not None else None, results)
#
# statuses.mask = is_python_in_tweet
#
# statuses['python'] = statuses['text'].apply(lambda s: is_token_in_tweet_text('python', s))
# statuses['java'] = statuses['text'].apply(lambda s: is_token_in_tweet_text('java', s))
# statuses['csharp'] = statuses['text'].apply(lambda s: is_token_in_tweet_text('csharp', s))
# statuses['fsharp'] = statuses['text'].apply(lambda s: is_token_in_tweet_text('fsharp', s))
#
#
# print statuses['python']
#
#
# slices = [
#     statuses['python'].value_counts()[True],
#     statuses['java'].value_counts()[True],
#     statuses['csharp'].value_counts()[True],
#     statuses['fsharp'].value_counts()[True]
# ]
