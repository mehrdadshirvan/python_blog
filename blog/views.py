import mysql.connector.connection
from MySQLdb import OperationalError
from django.shortcuts import render, redirect
import requests
import json
from django.db import connections
from django.http import HttpResponse

# Create your views
from blog.models import products
from my_site import settings


def index(request):
    return render(request, "blog/index.html")

def posts(request):
    db_conn = connections['default']
    try:
        c = db_conn.cursor()
    except OperationalError:
        connected = False
    else:
        connected = True

    pass
    # return render(request, "blog/posts.html", {'products': pro})

def single_post(request):
    pass
