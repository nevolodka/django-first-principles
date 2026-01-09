import os

from django.contrib import admin
from django.core.handlers.wsgi import WSGIHandler
from django.shortcuts import render
from django.urls import path

from blogs.models import Blog, BlogPost

admin.site.register((Blog, BlogPost))

def index(request):
    return render(request, "index.html")


urlpatterns = [
    path("", index),
    path("admin/", admin.site.urls),
]

application = WSGIHandler()
