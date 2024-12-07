from django.contrib import admin
from django.urls import path
from vehicle import views

path('uploadimage/', views.upload_image, name='upload'),
path('showimage/', views.show_image, name='image'),