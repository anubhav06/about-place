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

# Create your views here.
def index(request):
    return HttpResponse('Index loaded!')