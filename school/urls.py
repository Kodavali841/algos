from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = 'school'

urlpatterns = [
    path('subjects/', views.index, name='index'),
    path('subjects/create/', views.create, name='create'),
    url(r'^assignment/$', views.assign, name='urlname')
]