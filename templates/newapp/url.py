from django.urls import path
from newapp import views
from django.contrib import admin
from django.contrib.auth import views as auth_views 




urlpatterns=[
path('',views.home,name=''),
path('registration',views.registration, name='registration'),
path('login',views.login, name='login'),
path('file',views.processing, name='file'),

path('logout',views.logout, name='logout'),
]