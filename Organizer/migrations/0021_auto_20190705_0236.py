# Generated by Django 2.1 on 2019-07-04 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0020_organiseevent_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organiseevent',
            old_name='user_id',
            new_name='us_id',
        ),
    ]
