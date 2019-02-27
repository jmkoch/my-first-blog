# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0009_remove_pub_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='pub',
            name='middlename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
