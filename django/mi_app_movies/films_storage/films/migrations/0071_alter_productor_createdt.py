# Generated by Django 4.0.5 on 2022-07-07 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0070_alter_productor_createdt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productor',
            name='createDT',
            field=models.CharField(default=datetime.datetime(2022, 7, 7, 13, 51, 31, 709196), max_length=32),
        ),
    ]
