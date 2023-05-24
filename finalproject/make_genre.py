# -*- coding: utf-8 -*-

import requests
import json

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinebucks.settings")

django.setup()

from movies.models import Genre

#장르 api에서 데이터 불러오기
def genre_get():
    URL = 'https://api.themoviedb.org/3/genre/movie/list' 
    
    
    params = {
    'api_key': '837a5bfab43141b15658e475af9b943c',
    'language' : 'ko',
    } 
    response = requests.get(URL,params=params).json()
    json_data = response.get('genres')
    print(json_data)
              
    for j in range(len(json_data)):
        Genre.objects.create(
            pk = json_data[j]['id'],
            name = json_data[j]['name']
        )


genre_get()
