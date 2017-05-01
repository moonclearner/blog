from django.contrib import admin

# Register your models here.
from models import Article
from models import Category


admin.site.register(Article)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'brief', 'created_date', 'image', 'image_tag']
    #  fields = ('name', 'brief', 'created_date', 'image')
    #  readonly_fields = ('image_tag',)


admin.site.register(Category, CategoryAdmin)
