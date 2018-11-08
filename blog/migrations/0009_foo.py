# Generated by Django 2.0.8 on 2018-11-08 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20181108_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mighty_name', models.CharField(max_length=255)),
                ('kingdoms_count', models.PositiveIntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
