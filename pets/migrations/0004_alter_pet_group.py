# Generated by Django 4.2.5 on 2023-10-03 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_remove_group_pet'),
        ('pets', '0003_pet_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='groups.group'),
        ),
    ]
