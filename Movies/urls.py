from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Movies, name='Movies'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('movie_details/<movie_id>', views.movie_details, name='movie_details'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('search_details/', views.search_details, name='search_details'),
]