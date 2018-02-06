# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mainannouncements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='公告标题')),
                ('desc', models.CharField(max_length=50, verbose_name='公告描述')),
                ('content', models.TextField(verbose_name='公告内容')),
                ('click_count', models.IntegerField(default=0, verbose_name='点击次数')),
                ('is_recommend', models.BooleanField(default=False, verbose_name='是否推荐')),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '公告',
                'verbose_name_plural': '公告',
                'ordering': ['-date_publish'],
            },
        ),
    ]