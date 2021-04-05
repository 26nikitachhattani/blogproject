from django.contrib import admin
from django.urls import path, include
from blogs.api.views import (blogListApiView,blogDetailApiView, awsimageView,RegisterAPI)
from blogs.api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('awsimage', views.awsimageView)

urlpatterns = [
    path('',blogListApiView, name='list'),
    path('detail/<int:pk>',blogDetailApiView, name='detail'),
    path('imageapi', include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
    # path('create',BlogCreate, name='createpost'),
    # path('file', FileUploadView, name="file")

]
