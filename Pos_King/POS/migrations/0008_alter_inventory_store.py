# Generated by Django 3.2.4 on 2021-06-18 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0007_auto_20210618_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='POS.store'),
        ),
    ]
