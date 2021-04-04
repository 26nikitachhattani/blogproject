from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    #--- this url for without api blog list
    path('' ,views.feed_show, name='feed'),
    #----this url for api blog list
    path('listapi',views.lists, name="listapi"),
    
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('post',views.post,name='post'),

    path('postapi',views.postapi,name='post'),

    path('profile_view',views.profile_view,name='profile_view'),
    path('postdetail/<int:_id>',views.post_detail,name='postdetail'),
    path('blog/<int:_id>', views.BlogDetailView, name='blog'),
    path('like/<likeid>', views.likeview, name='like'),
]
handler404 = 'blogs.views.error_404'