# Generated by Django 3.2.4 on 2021-06-29 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0022_alter_transactions_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='items',
        ),
        migrations.AddField(
            model_name='transactions',
            name='items',
            field=models.ManyToManyField(related_name='transactions', to='POS.Inventory'),
        ),
    ]