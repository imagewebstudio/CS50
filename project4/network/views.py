from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import User, Post, Comment
from django.core.paginator import Paginator
from django.core.serializers.json import DjangoJSONEncoder
import json
import sys
import traceback



@csrf_exempt
@login_required
def newpost(request):
    if request.method == "POST":
        data = json.loads(request.body)
        newpost = data.get("newpost")
        user = request.user
        Post.objects.create(user= user, text= newpost)
        x = { "status": "true"}
        data = json.dumps(x)
        return HttpResponse(data)
    return

@csrf_exempt
@login_required
def update(request, post_id):
    if request.method == "PUT":
        try:
            user = request.user
            post = Post.objects.get(pk= post_id)
            data = json.loads(request.body)
            like_posts = post.liked_by.all()
            unliked_posts = post.unliked_by.all()
            if data.get("like") is not None:
                if user not in like_posts:
                    post.liked_by.add(user)
                    if user in unliked_posts:
                        post.unliked_by.remove(user)
                        x = { "status": "2true" }
                    else:
                        x = { "status": "true" }
                    data = json.dumps(x)
                    return HttpResponse(data)
                else:
                    post.liked_by.remove(user)
                    x = { "status": "false"}
                    data = json.dumps(x)
                    return HttpResponse(data)
            if data.get("dislike") is not None:
                if user not in unliked_posts:
                    post.unliked_by.add(user)
                    if user in like_posts:
                        post.liked_by.remove(user)
                        x = { "status": "2true"}
                    else:
                        x = { "status": "true" }
                    data = json.dumps(x)
                    return HttpResponse(data)
                else:
                    post.unliked_by.remove(user)
                    x = { "status": "false"}
                    data = json.dumps(x)
                    return HttpResponse(data)
            if data.get("edit") is not None:
                if user == post.user:
                    text = data.get("edit")
                    post.text = text
                    post.save()
                    x = { "status": "true"}
                    data = json.dumps(x)
                    return HttpResponse(data)
            if data.get("commented") is not None:
                new_comment = Comment.objects.create(text = data.get("commented"), user = user, usersname = user.username,  listing = post)
                new_comment.save()
                x = { "status": "true"}
                data = json.dumps(x)
                return HttpResponse(data)
        except BaseException as ex:
                # Get current system exception
                ex_type, ex_value, ex_traceback = sys.exc_info()

                # Extract unformatter stack traces as tuples
                trace_back = traceback.extract_tb(ex_traceback)

                # Format stacktrace
                stack_trace = list()

                for trace in trace_back:
                    stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

                x = {"Stack trace": stack_trace}
                data = json.dumps(x)
                return HttpResponse(data)
        return HttpResponse(status=204)

    if request.method == "GET":
        try:
            post = Post.objects.get(pk= post_id)
            comment = Comment.objects.all().filter(listing= post).values()
            data = json.dumps(list(comment), cls=DjangoJSONEncoder)
            return HttpResponse(data)
        except BaseException as ex:
                # Get current system exception
                ex_type, ex_value, ex_traceback = sys.exc_info()

                # Extract unformatter stack traces as tuples
                trace_back = traceback.extract_tb(ex_traceback)

                # Format stacktrace
                stack_trace = list()

                for trace in trace_back:
                    stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

                x = {"Stack trace": stack_trace}
                data = json.dumps(x)
                return HttpResponse(data)

def index(request):
    try:
        id = request.user.id
        user = User.objects.get(pk=id)
        userpost = Post.objects.order_by("-time")
        paginator = Paginator(userpost, 10)
        page_obj = paginator.get_page(1)
        return render(request, "network/index.html", {
        "UPost":page_obj, "Vuser":user,
        })
    except:
        post = Post.objects.all().order_by("-time")
        return render(request, "network/index.html", {
        "Post":post
    })


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
            user = User.objects.create_user(username, email, password, dob = request.POST["dob_date"])
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def profile(request):
    user = User.objects.get(pk=request.user.id)
    following = user.following.all()
    followedby = user.followed_by.all()
    return render(request, "network/profile.html", {
    "Following":following, "Followedby":followedby
    })
def public(request, page_number):
        try:
            allpost = Post.objects.all().order_by("-time")
            paginator = Paginator(allpost, 10)
            page_obj = paginator.get_page(page_number)
            return render(request, "network/public.html", {
            "Post":page_obj
            })
        except:
            post = Post.objects.all()
            return render(request, "network/public.html", {
            "Post":post
        })

@login_required
def following(request, page_number):
        try:
            user = User.objects.get(pk=request.user.id)
            following = user.following.all()
            followingpost = []
            allpost = Post.objects.all().order_by("-time")
            for i in range(len(allpost)):
                if allpost[i].user in following:
                    followingpost.append(allpost[i])
            paginator = Paginator(followingpost, 10)
            page_obj = paginator.get_page(page_number)
            return render(request, "network/following.html", {
            "Post":page_obj
            })
        except:
            return render(request, "network/following.html", {
            "Post":""
            })
def viewuser(request,user_id, page_number):
        try:
            user = User.objects.get(pk=user_id)
            userpost = Post.objects.filter(user=user).order_by("-time")
            paginator = Paginator(userpost, 10)
            page_obj = paginator.get_page(page_number)
            return render(request, "network/viewuser.html", {
            "Post":page_obj, "Vuser":user,
            })
        except:
            message = "Could not get users profile."
            return render(request, "network/index.html", {
            "message":message
            })


@csrf_exempt
@login_required
def follow(request,user_id):
    if request.method == "PUT":
        try:
            followuser = User.objects.get(pk=user_id)
            if not isinstance(followuser, User):
                x = { "followed": "notuser"}
                data = json.dumps(x)
                return HttpResponse(data)
            user = User.objects.get(pk=request.user.id)
            userfollowing = user.following.all()
            if not isinstance(user, User):
                x = { "followed": "notuser2"}
                data = json.dumps(x)
                return HttpResponse(data)
            if followuser in userfollowing:
                user.following.remove(followuser)
                x = { "followed": "not"}
                data = json.dumps(x)
                return HttpResponse(data)
            else:
                user.following.add(followuser)
                x = { "followed": "true"}
                data = json.dumps(x)
                return HttpResponse(data)
        except BaseException as ex:
                # Get current system exception
                ex_type, ex_value, ex_traceback = sys.exc_info()

                # Extract unformatter stack traces as tuples
                trace_back = traceback.extract_tb(ex_traceback)

                # Format stacktrace
                stack_trace = list()

                for trace in trace_back:
                    stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

                x = {"Stack trace": stack_trace}
                data = json.dumps(x)
                return HttpResponse(data)
    else:
        x = { "followed": "error2"}
        data = json.dumps(x)
        return HttpResponse(data)
