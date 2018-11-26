from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('movies/', views.movie_list, name = 'movie-list'),
    path('movies/<pk>/', views.movie_detail, name = 'movie-detail'),
    path('watch_list/<username>/', views.watch_list, name = 'watch_list'),
    path('watch_list_add/<username>/<pk>/', views.watch_list_add, name = 'add_to_watch_list'),
]

