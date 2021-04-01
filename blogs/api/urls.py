from django.contrib import admin
from django.urls import path
from blogs.api.views import (
    blogListApiView,
    blogDetailApiView
)

urlpatterns = [
    path('',blogListApiView, name='list'),
    path('detail/<int:pk>',blogDetailApiView, name='list'),
]
