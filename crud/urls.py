from django.urls import path

from . import views

# app_name = 'mysecapp'
urlpatterns = [
    path('', views.home,name='record'),
    path('delete/<int:id>/', views.delete_data,name='deletedata'),
    path('<int:id>/', views.update_data,name='updatedata'),

]

