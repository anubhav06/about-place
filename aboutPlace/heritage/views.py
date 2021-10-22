import json
from django.contrib.auth import authenticate, login, logout
from django.core import paginator
from django.db import IntegrityError
from django.db.models import constraints
from django.db.models.fields import DateTimeField, IntegerField, TimeField
from django.db.utils import DatabaseError, Error
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import datetime

from .models import User

# Create your views here.
def index(request):
    return render(request, "heritage/index.html")

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
    pass