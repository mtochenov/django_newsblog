from django.db import models


class Weather(models.Model):
    city = models.CharField("город", max_length=56)

    def __str__(self):
        return self.title
