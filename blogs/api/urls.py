from django.contrib import admin
from django.urls import path, include
from blogs.api.views import (blogListApiView,blogDetailApiView)
from blogs.api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('awsimage', views.awsimageView)

urlpatterns = [
    path('',blogListApiView, name='list'),
    path('detail/<int:pk>',blogDetailApiView, name='detail'),
    path('imageapi', include(router.urls)),
    # path('create',BlogCreate, name='createpost'),
    # path('file', FileUploadView, name="file")

]
