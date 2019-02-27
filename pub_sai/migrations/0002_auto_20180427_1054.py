# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pub',
            old_name='key',
            new_name='citekey',
        ),
    ]
