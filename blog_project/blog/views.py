from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

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
    #post = Post.objects.get(id=pid)
    
    post = get_object_or_404(Post, pk=pid)
    #comments = Comment.objects.filter(post=post)
    comments = post.comment_set.all()
    
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'show_post.html', context)


# Create your views here.
def search_posts(request, q):
    posts = Post.objects.filter(title__icontains=q)
    context = {
        'posts': posts
    }
    return render(request, 'list_posts.html', context)
    