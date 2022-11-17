from django.shortcuts import render
from .models import News

news = [
    {
        "title": "Первый запис",
        "text":  "Текст первый запис",
        "date":  "1 january",
        "author": "Bob"
    },

    {
        "title": "Второй запис",
        "text":  "Текст второго записа",
        "date":  "2 january",
        "author": "Админ"
    }
]

def home(request):
    data = {
        "news": News.objects.all(),
        "title": "Главная страница блога" 
    }
    return render(request, "app_blog/home.html", data)


def contact(request):
    return render(request, "app_blog/contact.html", {"title": "Страница о нас"})
