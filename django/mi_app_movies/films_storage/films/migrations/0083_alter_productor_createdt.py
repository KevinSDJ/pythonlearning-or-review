# Generated by Django 4.0.5 on 2022-07-08 02:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0082_alter_productor_createdt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productor',
            name='createDT',
            field=models.CharField(default=datetime.datetime(2022, 7, 8, 2, 49, 22, 811842), max_length=32),
        ),
    ]
