# -*- coding: utf-8 -*-

import requests
import json

#영화 api에서 데이터 불러오기
def genre_get():
    URL = 'https://api.themoviedb.org/3/genre/movie/list' 
    genre_list =[]
    
    genre_params = {
                'api_key': '87a6de2c61ab30d3330dbc8e5e60a509',
                'language' : 'ko',
            }
    
    response = requests.get(URL,params=genre_params).json()
    json_data = response.get('genres')
    
    for i in range(len(json_data)):
        
        fields = {    
                'genres_id': json_data[i]['id'],
                'name': json_data[i]['name'],
                }
        
        #json저장할 때 꼭 이 형태로 해야함! (data구조)
        data = {
            "pk": json_data[i]['id'],
            "model": "genres.genre",
            "fields": fields
        }
        genre_list.append(data)
    
            
    ## json파일로 저장하기
    with open('genre.json', 'w', encoding='UTF-8') as t:
        json.dump(genre_list, t, ensure_ascii=False, indent=2)
    
genre_get()

            
            



