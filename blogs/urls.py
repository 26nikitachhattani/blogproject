from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.feed_show, name='feed'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('post',views.post,name='post'),
    path('profile_view',views.profile_view,name='profile_view'),
    path('postdetail/<int:_id>',views.post_detail,name='postdetail'),
    path('blog/<int:_id>', views.BlogDetailView, name='blog'),
    path('like/<likeid>', views.likeview, name='like'),
]
