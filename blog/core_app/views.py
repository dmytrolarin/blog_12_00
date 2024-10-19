from django.shortcuts import render

# Create your views here.
def show_home(request):
    username = 'Dima'
    category_list = ["Політика", "Спорт", "ІТ"]

    return render(
        request,
        "core_app/home.html",
        context = {
            "username": username,
            "categories": category_list
        }
    )

