from django.shortcuts import render, get_object_or_404
from .models import Post


def view_all_posts(request):
    all_posts = Post.objects.filter(published = True)
    return render(request, "post_app/all_posts.html", context = { 'all_posts': all_posts })

def view_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_app/view_post.html", context = { 'post': post})