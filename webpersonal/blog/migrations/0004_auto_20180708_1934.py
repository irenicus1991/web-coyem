# Generated by Django 2.0.2 on 2018-07-08 23:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180708_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fechas de publicación'),
        ),
    ]