# Generated by Django 3.1.7 on 2021-05-17 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_auto_20210517_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='users_name',
            new_name='usersname',
        ),
    ]
