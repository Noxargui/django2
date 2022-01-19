# -*- coding: utf-8 -*-

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:theme_id>/', views.detail, name='detail'),
    path('<int:question_id>/', views.response, name='response'),
]