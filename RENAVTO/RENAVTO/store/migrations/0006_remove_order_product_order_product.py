# Generated by Django 4.0.6 on 2022-07-30 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_order_city_alter_order_date_of_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='store.auto_part', verbose_name='Товари:'),
        ),
    ]
