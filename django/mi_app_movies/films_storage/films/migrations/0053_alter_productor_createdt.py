# Generated by Django 4.0.5 on 2022-07-05 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0052_alter_film_poster_alter_productor_createdt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productor',
            name='createDT',
            field=models.CharField(default=datetime.datetime(2022, 7, 5, 17, 34, 7, 403318), max_length=32),
        ),
    ]
