from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    url(r'^api/v1/twitter_status/', views.twitter_status,name="twitter_status"),
    # url(r'^api/v1/github_status/', views.github_status,name="github_status"),
    # url(r'^api/v1/fan_status/', views.fan_status,name="fan_status"),
)
