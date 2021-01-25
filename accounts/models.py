from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class City(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Profile(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, null=True)
    image = models.ImageField(upload_to='profile/', null=True)
    city = models.ForeignKey(
        City, related_name='user_city', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
