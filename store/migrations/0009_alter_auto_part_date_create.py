# Generated by Django 4.0.6 on 2022-08-01 00:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_auto_part_date_created_auto_part_date_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto_part',
            name='date_create',
            field=models.DateField(default=datetime.datetime(2022, 8, 1, 0, 10, 41, 775080), verbose_name='Останній раз змінено:'),
        ),
    ]