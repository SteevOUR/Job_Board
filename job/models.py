from typing import Sized
from django.db import models
from django.db.models.fields.files import ImageFileDescriptor

# Create your models here.
from django.utils.text import slugify
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Category(models.Model):

    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


JOB_TYPE = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
)


def image_upload(instance, filename):

    image_name, extension = filename.split(".")
    return "jobs_img/%s.%s" % (instance.id, extension)


class Job(models.Model):

    owner = models.ForeignKey(
        User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to=image_upload, Size=[49, 49])
    image = ResizedImageField(
        size=[80, 80], crop=['middle', 'center'], upload_to=image_upload, force_format='PNG')

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Apply(models.Model):

    job = models.ForeignKey(
        Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    website = models.URLField(max_length=100)
    cv = models.FileField(upload_to='apply/', max_length=100)
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
