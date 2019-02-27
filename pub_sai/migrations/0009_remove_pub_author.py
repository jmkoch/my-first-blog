# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0008_pub_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pub',
            name='author',
        ),
    ]
