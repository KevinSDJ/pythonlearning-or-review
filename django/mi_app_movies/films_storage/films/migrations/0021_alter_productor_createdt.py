# Generated by Django 4.0.5 on 2022-07-02 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0020_alter_productor_createdt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productor',
            name='createDT',
            field=models.CharField(default=datetime.datetime(2022, 7, 2, 19, 15, 35, 869783), max_length=32),
        ),
    ]
