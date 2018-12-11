# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 00:20:55 2018

@author: Anil Sharma
"""
from django.urls import path
from . import views
app_name='polls'
urlpatterns=[
        path('',views.index,name='index'),
        path('<int:question_id>/',views.detail,name='detail'),
        path('<int:question_id/results/',views.results,name='results'),
        path('<int:question_id>/vote/',views.vote,name='vote'),
        ]
