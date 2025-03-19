from django.urls import path

from .views import list_posts, list_todays_posts, list_pubished_posts, list_draft_posts 

urlpatterns = [
    path('posts/', list_posts, name='list_posts'), 
    path('posts/today/', list_todays_posts, name='list_todays_posts'), 
    path('posts/published/', list_pubished_posts, name='list_published_posts'),
    path('posts/draft/', list_draft_posts, name='list_draft_posts'),    
]
