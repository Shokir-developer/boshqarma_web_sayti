from django.shortcuts import render

def index(request):
    context = {}

    return render(request, 'index.html', context)


def news(request):
    context = {}

    return render(request, 'news.html', context)
