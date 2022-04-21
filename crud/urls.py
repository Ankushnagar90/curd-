from django.urls import path

from . import views

# app_name = 'mysecapp'
urlpatterns = [
    path('', views.home,name='record'),
]