from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    # return HttpResponse("<h4>Главная страница</h4>")
    data = {
        'title': 'Главная страница',
    }

    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'О себе',
    }
    return render(request, 'main/about.html', data)


def contacts(request):
    return render(request, 'main/contacts.html')
