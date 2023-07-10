from xml.etree.ElementInclude import include

import mysql.connector.connection
from MySQLdb import OperationalError
from django.shortcuts import render, redirect, get_object_or_404
import requests
import json
from django.db import connections
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CustomerForm,ProfileForm
from .models import Product, Customer,Customer
from django.views.generic import ListView

# Create your views
# from blog.models import Product

def ListView(ListView):
    model = Customer
    template_name = "blog/index.html"
    context_object_name = "profile"
    pass


def index(request):
    # cform = CustomerForm()
    cform = ProfileForm()
    return render(request, "blog/index.html",{'cform':cform})

def posts(request):
    posts = Product.objects.all().order_by('-id')
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


def store_file(file):
    with open('temp/image.jpg','wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)


def create_customer(request):
    if request.method == 'POST':
        # cform = CustomerForm(request.POST)
        # if cform.is_valid():
        #     Customer(name=cform.cleaned_data['name']).save()
        #     return HttpResponseRedirect('/')
        submited_form = ProfileForm(request.POST,request.FILES)
        if submited_form.is_valid():
            customer = Customer(avatar=request.FILES['avatar'])
            customer.save()
            return HttpResponseRedirect("/customer/create")
        else:
            return render(request, "/customer/create")
    else:
        # cform = CustomerForm()
        cform = ProfileForm()

    return render(request, "blog/index.html",{'cform':cform})

