from django.urls import path
from movies import views

app_name = 'movies'
urlpatterns = [
    path('movies/', views.movie_create),
    # path('movies/<int:movie_id>/', views.movie_detail),
]