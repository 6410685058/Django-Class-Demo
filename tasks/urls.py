from django.urls import paths
from . import  views

app_name = 'tasks'
urlpatterns = [
    path('', views.index),
    ]