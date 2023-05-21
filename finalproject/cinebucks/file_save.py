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
    URL = 'https://api.themoviedb.org/3/movie/top_rated'
    movie_list =[]
    for i in range(1, 51): #데이터 1000개 불러오기 (페이지변화)
        params = {
        'api_key': '837a5bfab43141b15658e475af9b943c',
        'language' : 'ko',
        'region' : 'KR',
        'page' : i,
        } 
        response = requests.get(URL,params=params).json()
        json_data = response.get('results')
        
        for j in range(20):
            #JSON 데이터의 필드 값을 모델 필드에 맞게 변환 및 매핑 (movie)
            movie_item = {
                'id' : json_data[j]['id'],
                'title': json_data[j]['title'],
                'overview': json_data[j]['overview'],
                'adult': json_data[j]['adult'],
                'poster_path': json_data[j]['poster_path'],
                'backdrop_path': json_data[j]['backdrop_path'],
                'vote_average': json_data[j]['vote_average'],
                'vote_count': json_data[j]['vote_count'],
                # 'runtime': json_data[j]['runtime'],
                'genre_ids' : json_data[j]['genre_ids']
                }
            
            movie_list.append(movie_item)

    return movie_list
movie_list = movie_get()

## json파일로 저장하기
with open('movie.json', 'w', encoding='UTF-8') as t:
    json.dump(movie_list, t, ensure_ascii=False, indent=2)
