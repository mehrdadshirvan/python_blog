import mysql.connector.connection
from MySQLdb import OperationalError
from django.shortcuts import render, redirect, get_object_or_404
import requests
import json
from django.db import connections
from django.http import HttpResponse

# Create your views
from blog.models import Product


def index(request):
    return render(request, "blog/index.html")

def posts(request):
    posts = Product.objects.all()
    return render(request, "blog/posts.html",{'posts':posts})

def create(request):
    new = Product(name='testw').save()
    # posts = Product.objects.all()
    # new = Product.objects.all()[0]
    # new.name = 'mehrdad'
    # new.save()
    # new.delete()
    # p = Product.objects.get(id='2')
    # p.name = 'mehrdad2'
    # p.save()

    return render(request, "blog/posts.html",)

def single_post(request,slug):
    post = get_object_or_404(Product, slug=slug)
    Product.objects.get(slug=slug).save()
    return render(request, "blog/posts-single.html",{
        'name':post.name,
    })

