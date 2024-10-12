from django.shortcuts import render

# Create your views here.

def render_all_authors(request):
    return render(request = request, template_name = "author_app/all_authors.html")

def render_view_author(request):
    return render(request = request, template_name = "author_app/view_author.html")