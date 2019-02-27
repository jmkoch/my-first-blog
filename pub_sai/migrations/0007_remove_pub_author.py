# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0006_auto_20180514_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pub',
            name='author',
        ),
    ]
