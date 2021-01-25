from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Info

# Register your models here.

admin.site.register(Info)
