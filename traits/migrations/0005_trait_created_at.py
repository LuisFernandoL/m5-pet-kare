# Generated by Django 4.2.5 on 2023-10-03 23:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0004_alter_trait_pets'),
    ]

    operations = [
        migrations.AddField(
            model_name='trait',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
