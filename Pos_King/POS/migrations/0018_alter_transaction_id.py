# Generated by Django 3.2.4 on 2021-06-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0017_rename_transactions_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
