# Generated by Django 3.2.4 on 2021-06-18 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0006_auto_20210618_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='cost',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='price',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
