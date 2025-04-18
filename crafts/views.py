from django.shortcuts import render
from django.views import generic
from .models import Category, Post, Comment


# Create your views here.
class Categories(generic.ListView):
    queryset = Category.objects.all()
    template_name = "crafts/categories.html"
