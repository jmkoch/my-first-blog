# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0004_auto_20180514_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='pub',
            name='firstname',
            field=models.TextField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pub',
            name='lastname',
            field=models.TextField(max_length=100, blank=True, null=True),
        ),
    ]
