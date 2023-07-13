from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import UserPosts,MyProfile,Comments,RecentSearch,Rating,FriendRequest
from .forms import ImageForm,ProfileForm,CommentsForm,RecentSearchForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.method=="GET":
            searchform=RecentSearchForm()
            commentform=CommentsForm()
            userposts=UserPosts.objects.all()
            users=User.objects.exclude(id=request.user.id)
            profile=MyProfile.objects.get(user=request.user)
            friends=profile.friends.all()
            return render(request,'index.html',{'userposts':userposts,'commentform':commentform, 'searchform':searchform ,'users':users ,'friends':friends})
    else:
        return redirect("login/")

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password= request.POST['password']
        user=auth.authenticate(username=username ,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid login')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        gmail = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['rpassword']
        if username!="":
            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"username already taken")
                    return redirect('register')
                elif User.objects.filter(email=gmail).exists():
                    messages.info(request, "gmail already taken")
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=gmail, password=password1)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request, "password incorrect")
                return redirect('register')
            return redirect('/')
        else:
            messages.info(request, "username cannot be empty")
            return redirect('register')
    else:
        return render(request,'register.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=ImageForm(request.POST,request.FILES)
            if form.is_valid():
                f=form.save(commit=False)
                f.user_id=request.user.id
                f.save()

                return redirect('/')

        else:
            form=ImageForm()
            return render(request,'post.html',{'form':form})
    else:
        messages.info(request,"Please login First")
        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')

def myposts(request):
    userposts= UserPosts.objects.filter(user_id=request.user.id)
    return render(request,'MyPosts.html',{'userposts':userposts})

def myprofile(request, pk=None):
    if request.user.is_authenticated:
        button_status = 'none'
        if pk:
            profile = MyProfile.objects.filter(user_id=pk)
            fprofile=MyProfile.objects.get(user=request.user)
            user=User.objects.get(pk=pk)

            if user not in fprofile.friends.all():
                button_status = 'not_friend'
                f=FriendRequest.objects.filter(to_user=user,from_user=request.user)
                # if we have sent him a friend request
                if FriendRequest.objects.filter(to_user=user,from_user=request.user).exists():
                   button_status = 'friend_request_sent'
            else:
                button_status = 'friend'
        else:
            profile=MyProfile.objects.filter(user_id=request.user.id)
        return render(request,'profile.html',{'profile':profile,'pk':pk,'button_status':button_status})
    else:
        messages.info(request, 'Login first')
        return redirect('/')

def editprofile(request):
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user_id = request.user.id
            f.save()
            return redirect('profile')
    else:
        form =ProfileForm()
    return render(request,'EditProfile.html',{'form':form})

def comment_details(request):
    if request.user.is_authenticated:
        comment=request.POST['comment']
        postid=request.POST['postid']
        comments=Comments(comment=comment,user_id=request.user.id,userposts_id=postid)
        comments.save()
        allcomments=Comments.objects.filter(userposts_id=postid)
        commentform = CommentsForm()
        return render(request,'comment.html',{'commentform':commentform ,'allcomments':allcomments})

    else:
        messages.info(request,'Login first')
        return redirect('/')

def searchuser(request):
    if request.user.is_authenticated:
        searchform = RecentSearchForm(request.POST)
        if searchform.is_valid():
            searchform.save()
        searcheduser=request.POST['searchuser']
        users = User.objects.all()
        for user in users:
            if searcheduser==str(user):
                user_id=user.id
                profile=MyProfile.objects.filter(user_id=user_id)
                return render(request, 'profile.html', {'profile': profile, 'pk': user.id})
                found='User Found'
                break
            else:
                found='User Not Found'
        messages.info(request,found)
        return redirect('/')

    else:
        messages.info(request, 'Login first')
        return redirect('/')

def rate_details(request,rate,postid):
    if request.user.is_authenticated:
        if Rating.objects.filter(user_id=request.user.id,userposts_id=postid).exists():
            updaterate=Rating.objects.get(user_id=request.user.id,userposts_id=postid)
            updaterate.rate=rate
            updaterate.save()
        else:
            rating=Rating(user_id=request.user.id,userposts_id=postid,rate=rate)
            rating.save()
        return redirect('/')
    else:
        messages.warning(request, 'Login first')
        return redirect('/')

def send_request(request,id):
    if request.user.is_authenticated:
        user=get_object_or_404(User,id=id)
        profile=MyProfile.objects.filter(user_id=id)
        frequest,created=FriendRequest.objects.get_or_create(to_user=user,from_user=request.user)
        return redirect('profile/{}'.format(id))

    else:
        messages.info(request, 'Login first')
        return redirect('/')

def cancel_request(request,id):
    if request.user.is_authenticated:
        user=get_object_or_404(User,id=id)
        frequest=FriendRequest.objects.filter(to_user=user,from_user=request.user).first()
        if frequest:
            frequest.delete()
        return redirect('profile/{}'.format(id))
    else:
        messages.info(request, 'Login first')
        return redirect('/')

def accept_request(request,id):
    if request.user.is_authenticated:
        from_user=get_object_or_404(User,id=id)
        frequest=FriendRequest.objects.filter(to_user=request.user,from_user=from_user).first()
        user1=frequest.to_user
        user2=from_user
        #user1.profile.friends.add(user2.profile)
        #user2.profile.friends.add(user1.profile)
        profile=MyProfile.objects.get(user=request.user)
        profile.friends.add(from_user)
        frequest.delete()
        return redirect('/')
    else:
        messages.info(request, 'Login first')
        return redirect('/')

def delete_request(request,id):
    if request.user.is_authenticated:
        from_user=get_object_or_404(User,id=id)
        frequest=FriendRequest.objects.filter(to_user=request.user,from_user=from_user).first()
        frequest.delete()
        return redirect('/')
    else:
        messages.info(request, 'Login first')
        return redirect('/')
def notifications(request):
    notifications=FriendRequest.objects.filter(to_user=request.user)
    posts=UserPosts.objects.filter(user_id=request.user.id)
    comments=[]
    for post in posts:
        comment=Comments.objects.filter(userposts_id=post.id)
        comments.append(comment)
    return render(request,'notification.html',{'notifications':notifications ,'comments':comments})
