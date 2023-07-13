
from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('',views.index),
    path('login/',views.login, name='login'),
    path('register/', views.register, name='register'),
    path('post/', views.post,name='post'),
    path('logout/', views.logout,name='logout'),
    path('post/myposts/',views.myposts ),
    path('profile/', views.myprofile, name='profile'),
    path('profile/<int:pk>/',views.myprofile ,name='profile_pk'),
    path('profile/editprofile/',views.editprofile ,name='editprofile'),
    path('comment_details/',views.comment_details,name='comment_details'),
    path('search/',views.searchuser,name='search'),
    path('rate_details/<int:rate>/<int:postid>/', views.rate_details, name='rate_details'),
    path('add_request/<int:id>',views.send_request,name='add_request'),
    path('cancel_request/<int:id>',views.cancel_request,name='cancel_request'),
    path('add_request/profile/<int:pk>', views.myprofile, name='add_request'),
    path('cancel_request/profile/<int:pk>',views.myprofile,name='cancel_request'),
    path('notifications/',views.notifications, name='notifications'),
    path('accept_request/<int:id>',views.accept_request,name='accept_request'),
    path('delete_request/<int:id>',views.delete_request,name='delete_request'),
]

