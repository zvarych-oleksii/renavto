# Generated by Django 4.0.6 on 2022-07-29 22:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_brand_of_car_img_of_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('nova_post_number', models.CharField(max_length=30)),
                ('oplata_on_post', models.BooleanField(default=True)),
                ('date_of_order', models.DateField(default=datetime.datetime.today)),
                ('quantity_total', models.IntegerField()),
                ('price_total', models.IntegerField()),
                ('phone_number', models.CharField(max_length=15)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.auto_part')),
            ],
        ),
    ]
