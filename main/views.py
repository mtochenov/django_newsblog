from django.shortcuts import render
import requests


def index(request):
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


def weather(request):
    """
    Получает данные о погоде с сейта openweathermap.org/ Данные по бесплатному тарифу.
    Данные обрабатываются в формате json.
    """
    appid = "8bfe1216baff61f145a193def0c5b772"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = "Moscow,ru"  # Moscow,ru id - 524901
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,  # TODO: реализовать отображение нескольких городов через цикл
        'temp': round(res['main']['temp'], 1),
        'pressure': round(((res['main']['pressure']) * 0.750063), 1),
        'wind': res['wind']['speed'],
        'icon': res['weather'][0]['icon'],
    }

    data = {
        'info': city_info,
        'title': 'Погода',
    }

    return render(request, "main/weather.html", data)
