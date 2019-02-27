# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pub', '0010_pub_middlename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pub',
            old_name='firstname',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='pub',
            old_name='lastname',
            new_name='lastName',
        ),
        migrations.RenameField(
            model_name='pub',
            old_name='middlename',
            new_name='middleName',
        ),
    ]
