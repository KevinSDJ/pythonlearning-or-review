# Generated by Django 4.0.5 on 2022-07-07 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0074_productor_slug_alter_productor_createdt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productor',
            name='createDT',
            field=models.CharField(default=datetime.datetime(2022, 7, 7, 15, 12, 47, 336530), max_length=32),
        ),
    ]