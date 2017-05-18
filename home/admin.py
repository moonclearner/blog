from django.contrib import admin

# Register your models here.
from models import Article
from models import Category
from models import Tag


admin.site.register(Article)
admin.site.register(Tag)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'brief', 'created_date', 'image', 'image_tag']
    #  fields = ('name', 'brief', 'created_date', 'image')
    #  readonly_fields = ('image_tag',)


admin.site.register(Category, CategoryAdmin)
