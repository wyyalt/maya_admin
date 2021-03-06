# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-11 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, verbose_name='菜单名称')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p', to='maya.Menu', verbose_name='父菜单')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, verbose_name='权限名称')),
                ('app_label', models.CharField(max_length=32, verbose_name='app名称')),
                ('app_name', models.CharField(max_length=32, verbose_name='model名称')),
                ('name', models.CharField(max_length=32, verbose_name='name名称')),
                ('args', models.CharField(blank=True, max_length=64, null=True, verbose_name='反向创建URL参数(元组格式)')),
                ('query_params', models.CharField(blank=True, max_length=128, null=True, verbose_name='其他参数')),
                ('url', models.CharField(max_length=128)),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='maya.Menu', verbose_name='所属菜单')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, verbose_name='角色')),
                ('permissions', models.ManyToManyField(blank=True, null=True, to='maya.Permission', verbose_name='拥有权限')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('roles', models.ManyToManyField(blank=True, null=True, to='maya.Role', verbose_name='拥有角色')),
            ],
        ),
    ]
