# Generated by Django 2.0.8 on 2018-11-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_foo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus', models.CharField(max_length=50, null=True)),
                ('species', models.CharField(max_length=50, null=True)),
                ('fruit_type', models.CharField(choices=[('Capsule', 'Capsule'), ('Berry', 'Berry')], default='none', max_length=50)),
            ],
            options={
                'permissions': (('view_trait', 'Can view trait'),),
            },
        ),
    ]
