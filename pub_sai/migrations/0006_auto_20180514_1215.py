# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0005_auto_20180514_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pub',
            name='firstname',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pub',
            name='lastname',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
    ]
