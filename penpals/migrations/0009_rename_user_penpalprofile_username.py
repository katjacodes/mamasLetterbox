# Generated by Django 3.2.9 on 2022-01-24 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('penpals', '0008_alter_penpalprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='penpalprofile',
            old_name='user',
            new_name='username',
        ),
    ]