# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 23:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.TextField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Liked_bys', models.ManyToManyField(related_name='liked', to='app1.User')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relation', to='app1.User')),
            ],
        ),
    ]
