# Generated by Django 3.2.12 on 2022-02-16 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_alter_coresettings_default_time_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='coresettings',
            name='mesh_device_group',
            field=models.CharField(blank=True, default='TacticalRMM', max_length=255, null=True),
        ),
    ]