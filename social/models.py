from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserPosts(models.Model):
    #id=models.IntegerField
    desc=models.CharField(max_length=100,blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,related_name='userposts')
    image = models.ImageField(upload_to='posts/')


class FriendRequest(models.Model):
    to_user=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='to_user')
    from_user=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='from_user')
    time_created=models.DateTimeField(auto_now_add=True)

'''class Friend(models.Model):
    friends = models.ManyToManyField(User)
    current_user=models.ForeignKey(User,related_name='current_user',on_delete=models.CASCADE)'''

class MyProfile(models.Model):
    name=models.CharField(max_length=100)
    profession=models.CharField(max_length=100)
    hobbies=models.CharField(max_length=150)
    profile_photo=models.ImageField(upload_to='profile')
    user=models.OneToOneField(to=User,on_delete=models.CASCADE,related_name='user')
    friends = models.ManyToManyField(User,blank=True)

class Comments(models.Model):
    comment=models.CharField(max_length=100)
    user=models.ForeignKey(to=User ,on_delete=models.CASCADE,related_name='user_comment')
    userposts=models.ForeignKey(to=UserPosts ,on_delete=models.CASCADE,related_name='userpost_comment')
    created_on = models.DateTimeField(auto_now_add=True)

class RecentSearch(models.Model):
    searchuser=models.CharField(max_length=100)

class Rating(models.Model):
    rate=models.IntegerField()
    user=models.ForeignKey(to=User ,on_delete=models.CASCADE,related_name='user_rate')
    userposts=models.ForeignKey(to=UserPosts ,on_delete=models.CASCADE,related_name='userpost_rate')
    created_on = models.DateTimeField(auto_now_add=True)