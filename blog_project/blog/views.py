from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils.text import slugify

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
    f = CommentForm(request.POST or None, initial={'post': post.pk})
    
    #comments = Comment.objects.filter(post=post)
    comments = post.comment_set.all()
    
    context = {
        'post': post,
        'comments': comments,
        'form': f,
    }
    
    if f.is_valid():
        f.save()
        return redirect('show_post', pid=post.id)
    
    return render(request, 'show_post.html', context)


# Create your views here.
def search_posts(request, q):
    posts = Post.objects.filter(title__icontains=q)
    context = {
        'posts': posts
    }
    return render(request, 'list_posts.html', context)
    
def create_post(request):
    form = PostForm(request.POST or None)
    c = {
        'f': form,
    }
    
    if form.is_valid():
        post = form.save(commit=False)
        post.slug = slugify(post.title)
        post.save()
        return redirect('show_post', pid=post.id)
    
    return render(request, 'create_post.html', c)
    
    
def edit_post(request, pid):
    post = get_object_or_404(Post, pk=pid)
    form = PostForm(request.POST or None,instance=post)
    c = {
        'f': form,
    }
    
    if form.is_valid():
        post = form.save(commit=False)
        post.slug = slugify(post.title)
        post.save()
        return redirect('show_post', pid=post.id)
    
    return render(request, 'create_post.html', c)
    
    
def edit_comment(request, cid):
    comment = get_object_or_404(Comment, pk=cid)
    form = CommentForm(request.POST or None, instance=comment)
    c = {
        'f': form,
    }
    
    if form.is_valid():
        form.save()
        return redirect('show_post', pid=comment.post.id)
    
    return render(request, 'create_post.html', c)
    
def delete_post(request, pid):
    post = get_object_or_404(Post, pk=pid)
    m = f"Are you sure you want to delete {post.title}"
    c = {
        'message': m,
    }
    
    if "confirm" in request.GET:
        post.delete()
        return redirect('list_posts')
    elif "cancel" in request.GET:
        return redirect('list_posts')
    return render(request, 'confirm.html', c)
   