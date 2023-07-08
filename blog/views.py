from django.shortcuts import render, redirect
import requests
import json

from django.http import HttpResponse

# Create your views
from blog.models import products


def index(request):
    return render(request, "blog/index.html")

def posts(request):
    pro= products.objects.all()
    print(pro)
    # return render(request, "blog/posts.html", {'products': pro})

def single_post(request):
    pass
