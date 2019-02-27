# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0003_auto_20180509_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pub',
            old_name='annote',
            new_name='annotate',
        ),
    ]
