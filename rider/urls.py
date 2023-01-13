from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('rider',RiderAPI.as_view())
]