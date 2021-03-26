from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Country(models.Model):
    country_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=20)

    def __str__(self):
        return self.country_name, self.country_code
