# Generated by Django 4.0.5 on 2022-07-05 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0056_alter_productor_createdt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='productor',
            name='createDT',
            field=models.CharField(default=datetime.datetime(2022, 7, 5, 18, 40, 3, 131792), max_length=32),
        ),
        migrations.AlterField(
            model_name='productor',
            name='image_photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
