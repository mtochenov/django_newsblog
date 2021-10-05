from django.shortcuts import render
import requests
import random
from .forms import Weather


def index(request):
    """ Отображение шаблона главной страницы """
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


def change_city():
    """This func choices random city from list for weather func and return exact city"""
    cities_list = [
        "Moscow,RU",
        "Velikiy Novgorod,RU",
        "Nizhniy Novgorod,RU",
        "Saint Petersburg,RU",
        "Kyiv,UA",
        "Minsk,BY",
        "Tivat,ME",
    ]
    city = random.choice(cities_list)
    return city


def translate_city_name(city):
    """This func translate city name from english to russian"""
    en_ru_names = {
        "Moscow,RU": "Московия",
        "Velikiy Novgorod,RU": "Великий Новгород",
        "Nizhniy Novgorod,RU": "Нижний Новгород",
        "Saint Petersburg,RU": "Санкт-Петерсбург",
        "Kyiv,UA": "Киев",
        "Minsk,BY": "Минск",
        "Tivat,ME": "Тиват, Черногория",
    }
    city_name = en_ru_names[city]
    return city_name


def weather(request):
    """
    Получает данные о погоде с сейта openweathermap.org/ Данные по бесплатному тарифу.
    Данные обрабатываются в формате json.
    """
    appid = "8bfe1216baff61f145a193def0c5b772"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = change_city()
    city_name = translate_city_name(city)

    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'city_name': city_name,
        'temp': round(res['main']['temp'], 1),
        'pressure': round(((res['main']['pressure']) * 0.750063), 1),  # Переводим в мм ртутного столба
        'wind': res['wind']['speed'],
        'icon': res['weather'][0]['icon'],
    }

    data = {
        'info': city_info,
        'title': 'Погода',
    }

    return render(request, "main/weather.html", data)
