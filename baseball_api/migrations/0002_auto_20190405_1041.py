# Generated by Django 2.2 on 2019-04-05 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseball_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batting',
            old_name='playerid',
            new_name='player',
        ),
        migrations.RenameField(
            model_name='pitching',
            old_name='playerid',
            new_name='player',
        ),
    ]
