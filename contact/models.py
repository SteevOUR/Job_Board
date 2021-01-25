from django.db import models
from django.urls.base import reverse

# Create your models here.


class Info(models.Model):

    location = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)

    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")

    def __str__(self):
        return self.location
