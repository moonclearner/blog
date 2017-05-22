from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from uuslug import slugify
import markdown2
import pdb


class Category(models.Model):
    name = models.CharField(max_length=50)
    brief = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='photos/', default='statics/images/default.jpg')
    newarticle = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="%s" width="200px"/>' % (self.image.url))
    image_tag.short_description = 'Image'


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, null=True, blank=True)
    tag = models.ManyToManyField('Tag')
    category = models.ForeignKey(Category)
    text = models.TextField()
    markdowntext = models.TextField(default='', null=True, blank=True)
    clicknums = models.IntegerField(default=0)
    hidden = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    lastarticle = models.IntegerField(blank=True, null=True)
    nextarticle = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-published_date']

    def publish(self):
        newcategory = Category.objects.get(name=self.category)
        if newcategory.newarticle:
            lastarticle = Article.objects.get(pk=newcategory.newarticle)
            self.lastarticle = newcategory.newarticle
            lastarticle.nextarticle = self.pk
            lastarticle.save()
        newcategory.newarticle = self.pk
        self.published_date = timezone.now()
        self.save()
        newcategory.save()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.markdowntext = markdown2.markdown(self.text, extras=["fenced-code-blocks", "toc", "numbering", "footnotes", "cuddled-lists"])
        super(Article, self).save(*args, **kwargs)

    def increase_click(self):
        self.clicknums += 1
        self.save()

    def __unicode__(self):
        return self.title
