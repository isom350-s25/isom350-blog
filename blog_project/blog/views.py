from datetime import date
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
    posts = Post.objects.filter(created_on__date=date.today())
    context = {
        'posts': posts
    }
    return render(request, 'list_posts.html', context)

def list_pubished_posts(request):
    posts = Post.objects.filter(status=1)
    context = {
        'posts': posts
    }
    return render(request, 'list_posts.html', context)

def list_draft_posts(request):
    posts = Post.objects.filter(status=0)
    context = {
        'posts': posts
    }
    return render(request, 'list_posts.html', context)

def show_post(request, pid):
    post = Post.objects.get(id=pid)
    context = {
        'post': post
    }
    return render(request, 'show_post.html', context)
    