# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-18 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20170506_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_date']},
        ),
        migrations.AddField(
            model_name='article',
            name='clicknums',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='markdowntext',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='default', max_length=40),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, to='home.Tag'),
        ),
    ]
