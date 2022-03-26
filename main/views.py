from django.shortcuts import render


def home(request):
    """ Отображение шаблона главной страницы """
    return render(request, 'main/home.html', {'title': 'Главная страница'})


def about(request):
    """ Отображение шаблона страницы about"""
    return render(request, 'main/about.html', {'title': 'О себе'})


def contacts(request):
    """ Отображение шаблона страницы контактов"""
    return render(request, 'main/contacts.html')
