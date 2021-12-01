from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('search/', views.search_category, name='search_category'),
]