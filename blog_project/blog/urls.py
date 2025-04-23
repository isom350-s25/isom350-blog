from django.urls import path

from .views import (list_posts, list_todays_posts, 
                    list_pubished_posts, list_draft_posts, 
                    show_post, search_posts, create_post,
                    edit_post, edit_comment, delete_post)

#from . import views # needs views. before every function

urlpatterns = [
    path('posts/', list_posts, name='list_posts'), 
    path('posts/today/', list_todays_posts, name='list_todays_posts'), 
    path('posts/published/', list_pubished_posts, name='list_published_posts'),
    path('posts/draft/', list_draft_posts, name='list_draft_posts'),
    path('post/show/single/<int:pid>/', show_post, name='show_post'),      
    path('search/<str:q>/', search_posts, name='search_posts'),
    path('create/', create_post, name='create_post'),
    path('post/edit/<int:pid>/', edit_post, name='edit_post'),      
    path('comment/edit/<int:cid>/', edit_comment, name='edit_comment'),      
    path('post/delete/<int:pid>/', delete_post, name='delete_post'),      

]
