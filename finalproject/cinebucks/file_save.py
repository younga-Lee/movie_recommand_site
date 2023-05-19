# -*- coding: utf-8 -*-
# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinebucks.settings")

# django.setup()

# from django.core.management import call_command
import requests
import json
#영화 api에서 데이터 불러오기
def movie_get():
    URL = 'https://api.themoviedb.org/3/tv/top_rated'
    result =[]
    for i in range(1, 51): #데이터 1000개 불러오기 (페이지변화)
        params = {
        'api_key': '837a5bfab43141b15658e475af9b943c',
        'language' : 'ko',
        'region' : 'KR',
        'page' : i,
        } 
        response = requests.get(URL,params=params).json()
        
        
        result += response.get('results')
    
    return result
print(movie_get())
