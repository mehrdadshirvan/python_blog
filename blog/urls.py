from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="blog-index"),
    path("posts",views.posts, name="blog-posts"),
    path("posts/<slug:slug>",views.single_post, name="blog-single-post")
]