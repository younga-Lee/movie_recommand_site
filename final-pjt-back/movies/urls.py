from django.urls import path
from movies import views

app_name = 'movies'
urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/search/', views.search),
    path('movies/filter/', views.filter_movies),
    
    path('movies/<int:movie_id>/', views.movie_detail),
    path('movies/<int:movie_id>/', views.comment_list),
    
    path('movies/<int:movie_id>/comments/', views.comment_create),
    path('movies/<int:movie_id>/comments/<int:comment_pk>/', views.comment_detail),
    
]