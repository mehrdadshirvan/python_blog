from django.urls import path
from . import views

urlspattern = [
    path('',views.index),
    path("posts",views.posts),
    path("posts/<slug:slug>",views.single_post)
]