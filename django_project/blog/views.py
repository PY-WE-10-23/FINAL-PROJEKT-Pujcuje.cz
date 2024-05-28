from django.shortcuts import render
from .models import Post
from .models import Item
from .models import *


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def category(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'blog/category.html', context)

def my_items(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/my_items.html', context)

def rent(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'blog/rent.html', context)

def my_orders(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'blog/rent.html', context)

def my_diary(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'blog/rent.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})