# Generated by Django 4.0.5 on 2022-07-02 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0016_alter_productor_createdt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productor',
            name='createDT',
            field=models.CharField(default=datetime.datetime(2022, 7, 2, 15, 14, 6, 989219), max_length=32),
        ),
    ]
