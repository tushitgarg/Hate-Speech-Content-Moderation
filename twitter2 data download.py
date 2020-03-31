#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 00:06:40 2020

@author: tushit
"""

import tweepy
import pandas as pd
import numpy as np
from tqdm import tqdm
import json

consumer_key= ""
consumer_key_secret= ""
access_token= ""
access_token_secret= ""
auth = tweepy.auth.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

df = pd.read_csv('NAACL_SRW_2016.csv',names=['id','label'])

text=[pd.NA]*df.shape[0]
df['text']=text

for i in tqdm(df.index):
    f = open('twitter1.txt','a')
    dic = {}
    try:
        id_= str(df.iloc[i,0])
        dic['id'] = id_
        dic['label'] = df.iloc[i,1]
        tweet_text = api.get_status(id).text
        dic['text'] = text
        print(dic)
        f.write(json.dumps(dic))
        f.close
    except:
        continue