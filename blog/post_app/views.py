from django.shortcuts import render

# Create your views here.


def view_all_posts(request):
    return render(request, "post_app/all_posts.html")

def view_post(request):
    return render(request, "post_app/view_post.html")