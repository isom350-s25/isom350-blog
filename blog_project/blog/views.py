from django.shortcuts import render
from .models import Post

# Create your views here.
def list_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'list_posts.html', context)

def list_todays_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'list_posts.html', context)

def list_pubished_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'list_posts.html', context)

def list_draft_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'list_posts.html', context)