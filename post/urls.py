from django.contrib import admin
from django.urls import path, include
from post import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('',include('django.contrib.auth.urls')),
    path('movies/',views.movies,name='dashboard'),
    path('<slug:post>',views.post_detail,name='post_detail'),
    path('register/',views.register,name='register'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('search/', views.post_search, name='post_search'),
]