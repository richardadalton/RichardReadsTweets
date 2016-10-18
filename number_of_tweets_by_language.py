import json
import pandas as panda
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
ax1 = fig.add_subplot(2,1,1)

#style the axes and labels of our plot
ax1.tick_params(axis='x', labelsize=15)
ax1.tick_params(axis='y', labelsize=10)
ax1.set_xlabel('Tweet Languages', fontsize=15)
ax1.set_ylabel('Number of tweets' , fontsize=15)
ax1.xaxis.label.set_color('#666666')
ax1.yaxis.label.set_color('#666666')
ax1.tick_params(axis='x', colors='#666666')
ax1.tick_params(axis='y', colors='#666666')
#style the title

#plot the top 10 tweet languages and appearance count using a bar chart
tweets_by_lang[:10].plot(ax=ax1, kind='bar', color='#FF7A00')

#color the spines (borders)
for spine in ax1.spines.values():
        spine.set_edgecolor('#666666')






tweets_by_country = statuses['country'].value_counts()

# add a plot area for our data on the figure - 1,1,1 means a single chart/graph
ax2 = fig.add_subplot(2,1,2)

#style the axes and labels of our plot
ax2.tick_params(axis='x', labelsize=15)
ax2.tick_params(axis='y', labelsize=10)
ax2.set_xlabel('Tweet Countries', fontsize=15)
ax2.set_ylabel('Number of tweets', fontsize=15)
ax2.xaxis.label.set_color('#666666')
ax2.yaxis.label.set_color('#666666')
ax2.tick_params(axis='x', colors='#666666')
ax2.tick_params(axis='y', colors='#666666')
#style the title

#plot the top 10 tweet languages and appearance count using a bar chart
tweets_by_country[:10].plot(ax=ax2, kind='bar', color='#FF7A00')

#color the spines (borders)
for spine in ax2.spines.values():
        spine.set_edgecolor('#666666')

# render the graph
plt.show()

