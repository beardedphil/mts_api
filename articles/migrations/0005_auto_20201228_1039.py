# Generated by Django 3.1.4 on 2020-12-28 16:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20201228_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='keywords',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=None),
        ),
    ]
