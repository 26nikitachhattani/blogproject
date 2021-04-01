from django.contrib import admin
from django.urls import path
from profiles.api.views import (
    profileListApiView
)

urlpatterns = [
    path('',profileListApiView, name='profile_list'),
]
