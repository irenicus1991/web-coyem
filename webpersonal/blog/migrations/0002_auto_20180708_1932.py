# Generated by Django 2.0.2 on 2018-07-08 23:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateField(default=datetime.datetime(2018, 7, 8, 23, 32, 38, 851186, tzinfo=utc), verbose_name='Fechas de publicación'),
        ),
    ]
