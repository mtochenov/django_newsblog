from django.shortcuts import render
import requests


cities_dict = {
    "Moscow,RU": "Москва",
    "Velikiy Novgorod,RU": "Великий Новгород",
    "Nizhniy Novgorod,RU": "Нижний Новгород",
    "Saint Petersburg,RU": "Санкт-Петерсбург",
    "Kyiv,UA": "Киев",
    "Minsk,BY": "Минск",
    "Tivat,ME": "Тиват, Черногория",
}


def weather(request):
    """
    Получает данные о погоде с сейта 'openweathermap.org' Данные по бесплатному тарифу.
    Данные обрабатываются в формате json.
    """
    if request.method == "POST":
        city = request.POST['location']

    else:
        city = "Moscow,RU"

    appid = "8bfe1216baff61f145a193def0c5b772"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city_name = cities_dict[city]

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

    return render(request, "weather/weather.html", data)
