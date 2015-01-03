# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20141204_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
    ]
