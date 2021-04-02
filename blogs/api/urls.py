from django.contrib import admin
from django.urls import path
from blogs.api.views import (
    blogListApiView,
    blogDetailApiView,
    BlogCreate

)

urlpatterns = [
    path('',blogListApiView, name='list'),
    path('detail/<int:pk>',blogDetailApiView, name='detail'),
    path('create',BlogCreate, name='createpost'),

]
