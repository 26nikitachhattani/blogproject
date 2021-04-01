from django.contrib import admin
from django.urls import path
from .views import ProfileListView, ProfileDetailView, follow_unfollow_profile, Showprofileview, Editprofilepageview
from django.conf import settings

app_name = 'profile'

urlpatterns = [
    path('',ProfileListView.as_view(), name='profile-list-view'),
    path('switch-follow/',follow_unfollow_profile, name='follow-unfollow-view'),
    path('show_user_proifile/<pk>',ProfileDetailView.as_view(), name='profile-detail-view'),
    path('show_self_profile/<int:pk>',Showprofileview.as_view(), name='profile-show-view'),
    path('show_edit_profile/<int:pk>',Editprofilepageview.as_view(), name='profile-edit-view'),
    
]
