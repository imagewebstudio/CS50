# Generated by Django 3.2.4 on 2021-06-29 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0012_transactions_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pin',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
