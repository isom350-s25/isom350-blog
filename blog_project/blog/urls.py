from django.urls import path

from .views import list_posts

urlpatterns = [
    path('posts/', list_posts, name='list_posts'),  
]
