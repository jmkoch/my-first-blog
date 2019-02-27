# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0002_auto_20180427_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pub',
            name='type',
            field=models.CharField(null=True, choices=[('article', 'article'), ('book', 'book'), ('incollection', 'incollection'), ('manual', 'manual'), ('misc', 'misc'), ('unpublished', 'unpublished')], max_length=100, blank=True),
        ),
    ]
