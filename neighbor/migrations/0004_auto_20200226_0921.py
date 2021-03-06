# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-26 09:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbor', '0003_join'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('description', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='join',
            old_name='hood_id',
            new_name='area_id',
        ),
        migrations.AlterField(
            model_name='areacode',
            name='user_profile',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='areas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='post_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbor.Areacode'),
        ),
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
