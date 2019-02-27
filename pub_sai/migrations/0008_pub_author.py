# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0007_remove_pub_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='pub',
            name='author',
            field=models.ManyToManyField(null=True, related_name='author', blank=True, to='pub.Person'),
        ),
    ]
