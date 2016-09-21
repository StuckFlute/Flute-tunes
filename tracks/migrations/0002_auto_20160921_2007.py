# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.ForeignKey(to='albums.Album', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='track',
            name='title',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='track',
            name='track_number',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='track',
            name='artists',
            field=models.ManyToManyField(to='tracks.Artist', blank=True),
        ),
        migrations.AddField(
            model_name='track',
            name='genres',
            field=models.ManyToManyField(to='tracks.Genre', blank=True),
        ),
    ]
