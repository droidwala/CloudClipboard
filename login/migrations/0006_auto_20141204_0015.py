# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20141204_0014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='views',
            new_name='viewsa',
        ),
    ]
