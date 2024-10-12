from django.urls import path 
from .views import view_all_posts, view_post

urlpatterns = [
    path('all_posts/', view_all_posts, name="all_posts"),
    path('view_post/', view_post)
]