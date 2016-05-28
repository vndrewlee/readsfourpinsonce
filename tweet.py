
# coding: utf-8

# In[1]:

from pymarkovchain import MarkovChain

mc = MarkovChain(dbFilePath='./database.pkl')

tweet_text = mc.generateString()

import json

with open('credentials.json') as data_file:    
    credentials = json.load(data_file)

import tweepy

auth = tweepy.OAuthHandler(consumer_key=credentials['tw_key'], consumer_secret=credentials['tw_secret'])

auth.set_access_token(
    key=credentials['tw_access_token'], 
    secret=credentials['tw_access_token_secret'])

tw = tweepy.API(auth)

tw.update_status(status=tweet_text)


# In[ ]:



