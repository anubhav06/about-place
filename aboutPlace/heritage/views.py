import json
from typing import Counter
from django.contrib.auth import authenticate, login, logout
from django.core import paginator
from django.db import IntegrityError
from django.db.models import constraints
from django.db.models.fields import DateTimeField, IntegerField, TimeField
from django.db.utils import DatabaseError, Error
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import datetime

from .models import User, Posts
from .extras import List

# Create your views here.
def index(request):

    if request.method == "POST":
        list = List.list
        if request.POST["country"] in list:
            if not request.POST["title"] or request.POST["title"].isspace() or not request.POST["country"] or not request.POST["content"] or request.POST["content"].isspace():
                return HttpResponseNotFound("<h1> Error! All the fields are required to be filled ! </h1>")
            else:
                entry = Posts(poster = request.user, title = request.POST["title"], content = request.POST["content"], country = request.POST["country"])
                entry.save()
            
        else:
            return HttpResponseNotFound('<h1> The country does not exist! </h1>')    
        
        return HttpResponseRedirect(reverse('index')) 
    else:
        countries = Posts.objects.all().values_list('country', flat=True).distinct()

        return render(request, "heritage/index.html", {
            "countries" : countries,
        })

# Login View
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
            return render(request, "heritage/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "heritage/login.html")

# Logout View
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Register View
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "heritage/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "heritage/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "heritage/register.html")



def newPage(request):
    # List of countries
    list = List.list
    return render(request, "heritage/newPage.html", {
        "list" : list,
    }) 


def country_page(request, country):

    posts = Posts.objects.filter(country = country)
    return render(request, 'heritage/countryPage.html', {
        "posts" : posts,
        "country" : country,
    })