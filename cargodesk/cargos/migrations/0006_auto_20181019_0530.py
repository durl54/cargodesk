# Generated by Django 2.1.2 on 2018-10-19 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0005_auto_20181019_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='info',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
