from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('settings', settings, name='settings'),
    path('upload', upload, name='upload'),
    path('follow', follow, name='follow'),
    path('search', search, name='search'),
    path('profile/<str:pk>', Profil, name='profile'),
    path('like-post', like_post, name='like-post'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('logout', Logout, name='logout'),
]