# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_names', models.CharField(blank=True, null=True, max_length=100)),
                ('middle_names', models.CharField(blank=True, null=True, max_length=100)),
                ('last_names', models.CharField(blank=True, null=True, max_length=100)),
                ('safe_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('abstract', models.TextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, null=True, max_length=100)),
                ('annote', models.TextField(blank=True, null=True)),
                ('booktitle', models.CharField(blank=True, null=True, max_length=100)),
                ('chapter', models.CharField(blank=True, null=True, max_length=100)),
                ('crossref', models.CharField(blank=True, null=True, max_length=100)),
                ('doi', models.CharField(blank=True, null=True, max_length=100)),
                ('edition', models.CharField(blank=True, null=True, max_length=100)),
                ('howpublished', models.CharField(blank=True, null=True, max_length=100)),
                ('institution', models.CharField(blank=True, null=True, max_length=100)),
                ('journal', models.CharField(blank=True, null=True, max_length=100)),
                ('key', models.CharField(unique=True, max_length=100)),
                ('keywords', models.CharField(blank=True, null=True, max_length=100)),
                ('month', models.CharField(blank=True, null=True, max_length=100)),
                ('note', models.TextField(blank=True, null=True)),
                ('number', models.CharField(blank=True, null=True, max_length=100)),
                ('organization', models.CharField(blank=True, null=True, max_length=100)),
                ('pages', models.CharField(blank=True, null=True, max_length=100)),
                ('publisher', models.CharField(blank=True, null=True, max_length=100)),
                ('school', models.CharField(blank=True, null=True, max_length=100)),
                ('series', models.CharField(blank=True, null=True, max_length=100)),
                ('title', models.CharField(blank=True, max_length=500)),
                ('type', models.CharField(blank=True, null=True, choices=[('article', 'article'), ('book', 'book'), ('inbook', 'inbook'), ('incollection', 'incollection'), ('manual', 'manual'), ('misc', 'misc'), ('phdthesis', 'phdthesis'), ('unpublished', 'unpublished')], max_length=100)),
                ('volume', models.CharField(blank=True, null=True, max_length=100)),
                ('year', models.CharField(blank=True, null=True, max_length=100)),
                ('url', models.CharField(blank=True, null=True, max_length=100)),
                ('safe_deleted', models.BooleanField(default=False)),
                ('author', models.ManyToManyField(blank=True, null=True, to='pub.Person', related_name='author')),
                ('editor', models.ManyToManyField(blank=True, null=True, to='pub.Person', related_name='editor')),
            ],
        ),
    ]
