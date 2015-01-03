# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20141204_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='viewsa',
            new_name='views',
        ),
    ]
