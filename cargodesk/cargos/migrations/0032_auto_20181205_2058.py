# Generated by Django 2.0.9 on 2018-12-05 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0031_auto_20181203_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
