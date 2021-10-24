from django.shortcuts import render


def home(request):
    """ Отображение шаблона главной страницы """
    data = {
        'title': 'Главная страница',
    }

    return render(request, 'main/home.html', data)


def about(request):
    data = {
        'title': 'О себе',
    }
    return render(request, 'main/about.html', data)


def contacts(request):
    return render(request, 'main/contacts.html')
