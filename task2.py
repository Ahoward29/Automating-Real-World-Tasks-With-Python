#! /usr/bin/env python3
import os 
import requests

BASEPATH = '/data/feedback/'
folder = os.listdir(BASEPATH)
list = []

for file in folder:
    with open(BASEPATH + file, 'r') as f:
        list.append({"title":f.readline().rstrip("\n"),
            "name":f.readline().rstrip("\n"),
            "date":f.readline().rstrip("\n"),
            "feedback":f.read().rstrip("\n")})

for item in list:
   response = requests.post('http://104.198.212.144/feedback/', json=item)
   response.raise_for_status()
