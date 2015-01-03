# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='activation_key',
            field=models.CharField(default=datetime.datetime(2014, 12, 26, 18, 28, 31, 287000, tzinfo=utc), max_length=40, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2014, 12, 26)),
            preserve_default=True,
        ),
    ]
