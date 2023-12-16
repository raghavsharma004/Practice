# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 15:39:09 2023

@author: raghav
"""
import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

for data in response.json()['items']:
    if data['answer_count'] == 0:
      print(data['title'])
      print(data['link'])
    else:
        print("skipped")
        print()
        
      


