from django import forms
from .models import UserPosts,MyProfile,Comments,RecentSearch
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
class ImageForm(forms.ModelForm):
    class Meta:
        model= UserPosts
        fields= ['desc','image']

class ProfileForm(forms.ModelForm):
    class Meta:
        model= MyProfile
        fields=['name','profession','hobbies','profile_photo']

class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['comment']

class RecentSearchForm(forms.ModelForm):
    class Meta:
        model=RecentSearch
        fields=['searchuser']

