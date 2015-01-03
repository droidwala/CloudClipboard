# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_remove_category_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='viewsa',
            new_name='likes',
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
