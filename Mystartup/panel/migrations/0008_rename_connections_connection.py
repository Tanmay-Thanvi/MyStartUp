# Generated by Django 4.0.4 on 2022-08-18 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0007_connections'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Connections',
            new_name='Connection',
        ),
    ]