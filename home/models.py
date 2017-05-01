from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=50)
    brief = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='photos/', default='default.jpg')

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="%s" width="200px"/>' % (self.image.url))
    image_tag.short_description = 'Image'


class Article(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
