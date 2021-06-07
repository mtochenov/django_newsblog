from django.db import models
from django.utils import timezone


class Articles(models.Model):
    title = models.CharField("Название", max_length=56)
    announce = models.CharField("Анонс", max_length=256)
    full_text = models.TextField("Текст статьи")
    date = models.DateTimeField("Дата и время", default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
