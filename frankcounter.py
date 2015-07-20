#!/usr/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint
import json

with open('CleanishFrank.json') as data_file:
    data = json.load(data_file)

globalp = []

for date, playlist in data.items():
    # frank = 0.0
    # notfrank = 0.0
    for song in playlist:
        if len(song.encode('ascii', 'ignore').split('-')) != 3:
            print song.encode('ascii', 'ignore')
        # if 'Frank Sinatra' in song.encode('ascii', 'ignore'):
            # frank +=1
            # print song.encode('ascii', 'ignore').split('-')
        # else:
        #     notfrank +=1
#
#     total = len(playlist)
#     print date, '- {:.1%}'.format(frank/total) , '- Sinatra'
#     globalp.append(frank/total)
#
# print sum(globalp)/len(globalp)
