import json
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Posts

import datetime

def index(request):
    posts = Posts.objects.all().order_by('-creation_datetime')
    post_paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_obj = post_paginator.get_page(page_number)

    return render(request, "network/index.html", {
        "page_obj": page_obj,
        "page_name": "index"
    })


def following(request):
    following_list = request.user.following.all()
    posts = Posts.objects.filter(user__in=following_list).order_by('-creation_datetime')
    post_paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_obj = post_paginator.get_page(page_number)

    return render(request, "network/index.html", {
        "page_obj": page_obj,
        "page_name": "following"
    })     


def new_post(request):
    user = request.user
    content = request.POST["post"]
    creation_datetime=datetime.datetime.now()
    
    Posts.objects.create(user=user, content=content,
                         creation_datetime=creation_datetime)

    return HttpResponseRedirect(reverse("index"))


def profile(request, username):
    this_user = User.objects.get(username=username) 
    following_list = (request.user.following.all() if request.user.is_authenticated 
                      else [])    

    return render(request, "network/profile.html", {
        "following_list": following_list,
        "this_user": this_user,
        "followers_count": this_user.followers.count(),
        "following_count": this_user.following.count(),
        "posts": this_user.posts.all().order_by('-creation_datetime')
    })


def follow(request, this_username):
    this_user = User.objects.get(username=this_username)

    request.user.following.add(this_user) 
    this_user.followers.add(request.user)    

    return HttpResponseRedirect(reverse("profile", args=[this_username]))


def unfollow(request, this_username): 
    this_user = User.objects.get(username=this_username)

    request.user.following.remove(this_user)    
    this_user.followers.remove(request.user)    

    return HttpResponseRedirect(reverse("profile", args=[this_username]))   

@csrf_exempt
def save_edit(request, post_id):
    try:
        this_post = Posts.objects.get(id=post_id)
    except Posts.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)
            
    data = json.loads(request.body)
    this_post.content = data["content"]
    this_post.save()

    return HttpResponse(status=200)


@csrf_exempt
def like(request, post_id):
    try:
        this_post = Posts.objects.get(id=post_id)
    except Posts.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)
            
    data = json.loads(request.body)
    this_post.likes += data["like_increase"]
    this_post.save()

    return HttpResponse(status=200)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
