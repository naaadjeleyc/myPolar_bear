from django.db import models

# Create your models here.

class country(models.Model):
    country_name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=10)


class series(models.Model):
    series_code = models.ForeignKey(country, on_delete=models.CASCADE)
    series_name = models.CharField(max_length=200)
    year = models.IntegerField(default=0)