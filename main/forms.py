import random


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
