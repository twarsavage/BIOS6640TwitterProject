# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:07:59 2016

@author: ubuntu
"""

#final graphs

import pandas as pd

#laod and format language definition file
lang = pd.read_csv('/home/ubuntu/Desktop/ISO639-1CSV.txt')
lang = lang.rename(columns = {'English':'language','alpha2':'lang'})
#subset language from original data
langsub = final['lang'].copy().to_frame()
#merge for language names
langGroup = pd.merge(langsub,lang, on='lang', how='left')
#group by language
langsummary = langGroup.groupby('language').count()
# convert to series
s = langsummary.ix[:,0]

s.sort(ascending=False)
#remove top four
s2 = s.ix[4:]



#turn interactive mode off
ioff()

import matplotlib
matplotlib.pyplot.ion()
matplotlib.pyplot.ioff()
matplotlib.is_interactive()

import matplotlib.pyplot as plt

fig, axes = plt.subplots(1,1)
#s.plot(kind='bar', ax=axes[0], color='k', alpha=0.7)
#s2.plot(kind='barh', ax=axes[1], color='k', alpha=0.7)
s.plot(kind='bar')
#s.plot(kind='barh', stacked=True, alpha=0.5)

plt.show()
plt.gcf()
plt.clf()

             
# aggregations for summary data
aggregations = {
    'spreadflag':'sum',
    'prevent':'sum',
    'bug':'sum',
    'science':'sum',
    'politic':'sum',
    'news':'sum',
    'olymp':'sum',
    'reprod':'sum',
    #'sentiment':'mean'
}                  

final2 = finaleng.copy()
final2['Group'] = 1
summary = final2.groupby('Group', as_index=False).agg(aggregations)
summary = summary.rename(columns = {'spreadflag':'Spread',
                                    'prevent':'Prevent',
                                    'bug':'Mosquito',
                                    'science':'Scientific',
                                    'politic':'Political',
                                    'news':'News',
                                    'olymp':'Olympics',
                                    'reprod':'Birth/Child',
                                    'Group':'key'
                                    })

summary = summary.transpose()
summary = summary.drop('key')
summary = summary.rename(columns = {0:'Count'})
summary.sort_values('Count',inplace=True,ascending=False)

fig, axes = plt.subplots(1,1)
#s.plot(kind='bar', ax=axes[0], color='k', alpha=0.7)
#s2.plot(kind='barh', ax=axes[1], color='k', alpha=0.7)
#summary.plot(kind='bar')
summary.plot(kind='barh', stacked=True, alpha=0.5)
plt.title('Tweet count by subject')

plt.savefig('/home/ubuntu/Desktop/SubjectTweet.png')
#plt.show()
#plt.gcf()
plt.clf()

#Sentiment data
finalengsamp2 = finalengsamp.copy()
finalengsamp2['Group'] = 1
summary = finalengsamp2.groupby('Group', as_index=False).agg(aggregations)
summary = summary.rename(columns = {'spreadflag':'Spread',
                                    'prevent':'Prevention',
                                    'bug':'Mosquitoes',
                                    'science':'Scientific',
                                    'politic':'Political',
                                    'news':'News',
                                    'olymp':'Olympics',
                                    'reprod':'Reproductive',
                                    'Group':'key'
                                    })

summary = summary.transpose()
summary = summary.drop('key')




# time vs sentiment
from datetime import datetime
from dateutil.parser import parse


finalengsamp3 = finalengsamp.copy()
finalengsamp3['Group'] = 1
finalengsamp3['Time'] = finalengsamp3['created_at'].map(parse)
finalengsamp3['Hour'] = map(lambda x: x.hour,finalengsamp3['Time'])

summary3 = finalengsamp3.groupby('Hour', as_index=False).agg({'sentiment':'mean','Group':'sum'})
summary3 = summary3.rename(columns = {'Group':'TweetCount'})

fig, ax1 = plt.subplots()
summary3.plot(x='Hour', y='TweetCount', kind='bar', ax=ax1)

ax2 = ax1.twinx()
summary3.plot(x='Hour',y='sentiment',kind='line', ax=ax2,c='r',linewidth=3)
plt.title('Tweet sentiment by hour')

plt.savefig('/home/ubuntu/Desktop/SentvsTime2.png')
#plt.show()
#plt.gcf()
plt.clf()

#add time graph here
col = ['created_at','id_str']
fullsub = data.ix[:,col].copy()
''' TROUBLE SHOOTING
for i in range(149358):
    try:
        parse(fullsub.ix[i,0])
    except:
        print i

found nulls in created_at field
'''
fullsub = fullsub.loc[fullsub['created_at'].notnull(),col] 
fullsub['Group'] = 1
fullsub['Time'] = fullsub['created_at'].map(parse)
#remove minutes and hours from time data
fullsub['datetime'] = map(lambda x: x.strftime('%a %b %d %H:00:00 %Y'),fullsub['Time'])
fullsubGrp = fullsub.groupby('datetime', as_index=False).agg({'Group':'sum'})
fullsubGrp = fullsubGrp.rename(columns = {'Group':'Count'})


TweetCount = fullsubGrp.iloc[:,1]#fullsubGrp.Count.values
TweetDT = fullsubGrp.iloc[:,0].map(parse).dt.to_pydatetime()
dates = matplotlib.dates.date2num(TweetDT)


fig, axes = plt.subplots(1,1)
axes.set_ylim([0,3000])
plt.grid(b=True,which='major',color='b',linestyle='-')

#fullsubGrp.plot(kind='bar', stacked=True, alpha=0.5)
plt.title('Tweet count by time(tweets per hour)')

plt.plot_date(dates,TweetCount, 'ro')



plt.savefig('/home/ubuntu/Desktop/TweetbyTime.png')
#plt.show()
plt.gcf()
plt.clf()

