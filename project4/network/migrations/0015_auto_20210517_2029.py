# Generated by Django 3.1.7 on 2021-05-17 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0014_auto_20210517_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='usersname',
        ),
    ]
