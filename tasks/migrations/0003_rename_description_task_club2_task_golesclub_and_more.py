# Generated by Django 4.1.3 on 2023-11-16 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_datedcompleted_task_datecompleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='club2',
        ),
        migrations.AddField(
            model_name='task',
            name='golesclub',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='golesclub2',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
