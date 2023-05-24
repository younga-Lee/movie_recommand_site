from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('<str:username>/', views.user_detail, name='profile'),
    # path('getuser/<str:username>/', views.get_user, name='getuser'),
]