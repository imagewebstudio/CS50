# Generated by Django 3.2.4 on 2021-06-29 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0014_alter_transactions_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
