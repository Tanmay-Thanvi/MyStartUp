# Generated by Django 4.0.4 on 2022-08-21 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0008_rename_connections_connection'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Mobile',
            field=models.IntegerField(default=0),
        ),
    ]
