# -*- coding: utf-8 -*-

import requests
import json

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinebucks.settings")

django.setup()

from movies.models import Movie

#영화 api에서 데이터 불러오기
def movie_get():
    URL = 'https://api.themoviedb.org/3/movie/popular' 
    # URL = 'https://api.themoviedb.org/3/movie/now_playing' 
    movie_list =[]
    
    for i in range(1, 3): #데이터 1000개 불러오기 (한 페이지당 20개 있었음)
        params = {
        'api_key': '837a5bfab43141b15658e475af9b943c',
        'language' : 'ko',
        'region' : 'KR',
        'page' : i,
        } 
        response = requests.get(URL,params=params).json()
        json_data = response.get('results')
        
        for j in range(20):
            movie_id = json_data[j]['id']

            # 이미 존재하는 ID의 영화인 경우 건너뛰기
            if Movie.objects.filter(id=movie_id).exists():
                continue            
            
            print(json_data[j]['title'])
            #영화 디테일API에서 런타임 불러오기
            DETAIL_URL = 'https://api.themoviedb.org/3/movie/' + str(movie_id)
        
            detail_params = {
                'api_key': '87a6de2c61ab30d3330dbc8e5e60a509',
                'language' : 'ko',
            }
            
            detail_response = requests.get(DETAIL_URL,params=detail_params).json()
            
            Movie.objects.create(
                pk = json_data[j]['id'],
                title = json_data[j]['title'],
                overview = json_data[j]['overview'],
                adult = json_data[j]['adult'],
                poster_path = json_data[j]['poster_path'],
                backdrop_path = json_data[j]['backdrop_path'],
                vote_average = json_data[j]['vote_average'],
                vote_count = json_data[j]['vote_count'],
                runtime = detail_response['runtime'],
            )
    #         fields = {
    #             'title': json_data[j]['title'],
    #             'overview': json_data[j]['overview'],
    #             'adult': json_data[j]['adult'],
    #             'poster_path': json_data[j]['poster_path'],
    #             'backdrop_path': json_data[j]['backdrop_path'],
    #             'vote_average': json_data[j]['vote_average'],
    #             'vote_count': json_data[j]['vote_count'],
    #             'runtime': detail_response['runtime'],

    #             }
            
    #         #json저장할 때 꼭 이 형태로 해야함! (data구조)
    #         data = {
    #             "pk": json_data[j]['id'],
    #             "model": "movies.movie",
    #             "fields": fields
    #         }
    #         movie_list.append(data)
            
    # ## json파일로 저장하기
    # with open('boxmovie.json', 'w', encoding='UTF-8') as t:
    #     json.dump(movie_list, t, ensure_ascii=False, indent=2)

movie_get()


