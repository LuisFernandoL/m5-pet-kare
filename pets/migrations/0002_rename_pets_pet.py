# Generated by Django 4.2.5 on 2023-10-03 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_rename_groups_group'),
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pets',
            new_name='Pet',
        ),
    ]