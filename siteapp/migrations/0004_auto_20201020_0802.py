# Generated by Django 3.1.1 on 2020-10-20 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0003_auto_20201020_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(verbose_name='Post slug'),
        ),
    ]
