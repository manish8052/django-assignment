from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('requester',RequesterAPI.as_view()),
    path('my-assets',MyAssetAPI.as_view()),
    path('matched-assets',MatchedAssetAPI.as_view())
]