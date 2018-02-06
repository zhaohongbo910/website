# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-07 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_singlenum', models.CharField(max_length=50, verbose_name='出库单号')),
                ('out_theme', models.CharField(max_length=50, verbose_name='出库主题')),
                ('sales_invoice', models.CharField(max_length=50, verbose_name='销售发货单')),
                ('customer_name', models.CharField(max_length=50, verbose_name='客户名称')),
                ('modules', models.CharField(max_length=50, verbose_name='源单类型')),
            ],
            options={
                'verbose_name': '库存管理',
                'verbose_name_plural': '库存管理',
            },
        ),
    ]
