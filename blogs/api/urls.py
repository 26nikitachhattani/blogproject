from django.contrib import admin
from django.urls import path, include
from blogs.api.views import (blogListApiView,blogDetailApiView, awsimageView,RegisterAPI)
from blogs.api import views
from rest_framework import routers
from knox import views as knox_views
from .views import LoginAPI


router = routers.DefaultRouter()
router.register('awsimage', views.awsimageView)

urlpatterns = [
    path('',blogListApiView, name='list'),
    path('detail/<int:pk>',blogDetailApiView, name='detail'),
    path('imageapi', include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    
    # path('create',BlogCreate, name='createpost'),
    # path('file', FileUploadView, name="file")

]
