from django.shortcuts import render
from .models import Post

# Create your views here.
def list_posts(request):
    
    # you need to fetch the posts
    # from the database here
    # and pass them to the template
    
    posts = Post.objects.filter(title__icontains='post')
    context = {
        'posts': posts
    }
    
    return render(request, 'list_posts.html', context)