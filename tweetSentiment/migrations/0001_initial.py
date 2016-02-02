# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(default=b'', max_length=200)),
                ('user', models.CharField(default=b'', max_length=200)),
                ('text', models.CharField(default=b'', max_length=500)),
                ('latitude', models.CharField(default=b'', max_length=255)),
                ('longitude', models.CharField(default=b'', max_length=255)),
                ('sicDescription', models.CharField(default=b'', max_length=100)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('lastModifiedTime', models.DateTimeField(auto_now=True)),
                ('sentiment_exist', models.BooleanField(default=False)),
                ('sentiment', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TweetAuth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appName', models.CharField(default=b'', max_length=200)),
                ('appSecret', models.CharField(default=b'', max_length=200)),
                ('appKey', models.CharField(default=b'', max_length=200)),
                ('appAccessToken', models.CharField(default=b'', max_length=200)),
                ('appAccessSecret', models.CharField(default=b'', max_length=200)),
            ],
        ),
    ]
