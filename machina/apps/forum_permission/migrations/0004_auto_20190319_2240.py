# Generated by Django 2.1.7 on 2019-03-20 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum_permission', '0003_remove_forumpermission_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumpermission',
            name='is_global',
        ),
        migrations.RemoveField(
            model_name='forumpermission',
            name='is_local',
        ),
    ]
