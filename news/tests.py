from django.test import TestCase
from django.urls import reverse, resolve

from .views import *


class TestUrls(TestCase):

    def test_news_list_resolved(self):
        url = reverse('news_list')
        self.assertEquals(resolve(url).func.view_class, NewsListView)

    def test_news_detail_resolved(self):
        url = reverse('news_detail', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, NewsDetailView)

    def test_news_add_resolved(self):
        url = reverse('create')
        self.assertEquals(resolve(url).func, news_create)

    def test_news_update_resolved(self):
        url = reverse('news_update', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, NewsUpdateView)

    def test_news_delete_resolved(self):
        url = reverse('news_delete', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, NewsDeleteView)
