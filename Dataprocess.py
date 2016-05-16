#Create Final data set

import json
import pandas as pd

#tweets_data_path = 'C:/Users/Mac/Desktop/testzika2.txt'

#tweets_data_path = '/home/ubuntu/Desktop/allzika.txt'
#tweets_data_path = '/home/ubuntu/Desktop/testzika2.txt'
#tweets_data_path = '/home/ubuntu/Desktop/zikadata.txt'
#tweets_data_path = '/home/ubuntu/Desktop/zikadata2.txt'
tweets_data_path = '/home/ubuntu/Desktop/zikadata3.txt'


# from original data scanner
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
    

#load data 
data = pd.DataFrame(pd.io.json.json_normalize(tweets_data))




#create column lists       
#original column names
origTwCol = ['coordinates.coordinates',
           'created_at',
           'place.bounding_box.coordinates',
           'place.full_name',
           'lang',
           'id_str',
           'user.id_str',
           'user.listed_count',
           'user.followers_count',
           'user.friends_count',
           'retweet_count',
           'favorite_count',
           'text',
           'is_quote_status'
           ]
#orinal for quote
quotTwCol = ['quoted_status.coordinates.coordinates',
           'quoted_status.created_at',
           'quoted_status.place.bounding_box.coordinates',
           'quoted_status.place.full_name',
           'quoted_status.lang',
           'quoted_status.id_str',
           'quoted_status.user.id_str',
           'quoted_status.user.listed_count',
           'quoted_status.user.followers_count',
           'quoted_status.user.friends_count',
           'quoted_status.retweet_count',
           'quoted_status.favorite_count',
           'quoted_status.text',
           'quoted_status.is_quote_status'
           ]
           
#original for retweet of quote
RTQtTwCol = ['retweeted_status.quoted_status.coordinates.coordinates',
           'retweeted_status.quoted_status.created_at',
           'retweeted_status.quoted_status.place.bounding_box.coordinates',
           'retweeted_status.quoted_status.place.full_name',
           'retweeted_status.quoted_status.lang',
           'retweeted_status.quoted_status.id_str',
           'retweeted_status.quoted_status.user.id_str',
           'retweeted_status.quoted_status.user.listed_count',
           'retweeted_status.quoted_status.user.followers_count',
           'retweeted_status.quoted_status.user.friends_count',
           'retweeted_status.quoted_status.retweet_count',
           'retweeted_status.quoted_status.favorite_count',
           'retweeted_status.quoted_status.text',
           'retweeted_status.quoted_status.is_quote_status'
           ]
           
#quote of retweet of quote and
#original for RT
RTwCol = ['retweeted_status.coordinates.coordinates',
           'retweeted_status.created_at',
           'retweeted_status.place.bounding_box.coordinates',
           'retweeted_status.place.full_name',
           'retweeted_status.lang',
           'retweeted_status.id_str',
           'retweeted_status.user.id_str',
           'retweeted_status.user.listed_count',
           'retweeted_status.user.followers_count',
           'retweeted_status.user.friends_count',
           'retweeted_status.retweet_count',
           'retweeted_status.favorite_count',
           'retweeted_status.text',
           'retweeted_status.is_quote_status'
           ]
           

#original from orig - build table, rename and add flags
O1 = data.loc[(data['retweeted_status.id_str'].isnull()) &
        (data['quoted_status.id_str'].isnull()) &
        (data['retweeted_status.quoted_status.id_str'].isnull()),origTwCol].copy()
O1.columns = origTwCol
#original form retweet
O2 = data.loc[(data['retweeted_status.id_str'].notnull()) &
        (data['quoted_status.id_str'].isnull()) &
        (data['retweeted_status.quoted_status.id_str'].isnull()),RTwCol].copy()
O2.columns = origTwCol
#retweet from retweet
#O2a = data.loc[(data['retweeted_status.id_str'].notnull()) &
#        (data['quoted_status.id_str'].isnull()) &
#        (data['retweeted_status.quoted_status.id_str'].isnull()),origTwCol].copy()
#O2a.columns = origTwCol
#original from quote - build table, rename and add flags
O3 = data.loc[(data['retweeted_status.id_str'].isnull()) &
        (data['quoted_status.id_str'].notnull()) &
        (data['retweeted_status.quoted_status.id_str'].isnull()),quotTwCol].copy()
O3.columns = origTwCol
#quote from quote - build table, rename and add flags
O3a = data.loc[(data['retweeted_status.id_str'].isnull()) &
        (data['quoted_status.id_str'].notnull()) &
        (data['retweeted_status.quoted_status.id_str'].isnull()),origTwCol].copy()
O3a.columns = origTwCol
#original from retweet of quote
O4 = data.loc[(data['retweeted_status.id_str'].notnull()) &
        (data['quoted_status.id_str'].isnull()) &
        (data['retweeted_status.quoted_status.id_str'].notnull()),RTQtTwCol].copy()
O4.columns = origTwCol
#quote from retweet of quote
O4a = data.loc[(data['retweeted_status.id_str'].notnull()) &
        (data['quoted_status.id_str'].isnull()) &
        (data['retweeted_status.quoted_status.id_str'].notnull()),RTwCol].copy()
O4a.columns = origTwCol
#retweet from retweet of quote
#O4b = data.loc[(data['retweeted_status.id_str'].notnull()) &
#        (data['quoted_status.id_str'].isnull()) &
#        (data['retweeted_status.quoted_status.id_str'].notnull()),origTwCol].copy()
#O4b.columns = origTwCol


# merge datasets
#O1 and O3
combined = pd.concat([O1, O2, O3, O3a, O4, O4a], ignore_index=True)

aggregations = {
    'coordinates.coordinates': lambda x: max(x),
    'place.bounding_box.coordinates': lambda x: max(x),
    'place.full_name': lambda x: max(x),
    'user.listed_count': lambda x: max(x),
    'user.followers_count': lambda x: max(x),
    'user.friends_count': lambda x: max(x),
    'retweet_count': lambda x: max(x),
    'favorite_count': lambda x: max(x),
    'text': 'first'
}

final = combined.groupby(['id_str',
                  'created_at',
                  'is_quote_status',
                  'lang',
                  'user.id_str'
                  ], as_index=False).agg(aggregations)
    



