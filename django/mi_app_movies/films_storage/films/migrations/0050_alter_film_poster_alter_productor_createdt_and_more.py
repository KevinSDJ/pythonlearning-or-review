# Generated by Django 4.0.5 on 2022-07-05 02:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0049_alter_productor_createdt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='poster',
            field=models.ImageField(null=True, upload_to='media/movies_poster'),
        ),
        migrations.AlterField(
            model_name='productor',
            name='createDT',
            field=models.CharField(default=datetime.datetime(2022, 7, 5, 2, 30, 1, 470704), max_length=32),
        ),
        migrations.AlterField(
            model_name='productor',
            name='image_photo',
            field=models.ImageField(null=True, upload_to='media/productors'),
        ),
    ]