# Generated by Django 4.2.5 on 2023-10-03 20:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_rename_groups_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
