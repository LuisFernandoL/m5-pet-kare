# Generated by Django 4.2.5 on 2023-10-03 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_group_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='pet',
        ),
    ]
