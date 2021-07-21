# Generated by Django 3.2.1 on 2021-07-21 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0007_auto_20210721_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerttemplate',
            name='agent_script_actions',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='alerttemplate',
            name='check_script_actions',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='alerttemplate',
            name='task_script_actions',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
