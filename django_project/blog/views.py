from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def category(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/category.html', context)

def my_items(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/my_items.html', context)

def rent(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/rent.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})