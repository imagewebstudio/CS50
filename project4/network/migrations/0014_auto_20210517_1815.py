# Generated by Django 3.1.7 on 2021-05-17 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_auto_20210517_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='listing',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='usersname',
            new_name='name',
        ),
    ]