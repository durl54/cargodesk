# Generated by Django 2.0.9 on 2018-11-08 18:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0023_auto_20181108_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='closed_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
