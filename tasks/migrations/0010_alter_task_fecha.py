# Generated by Django 4.1.3 on 2023-11-16 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_task_fecha_alter_task_golesclub_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='fecha',
            field=models.TextField(max_length=201, null=True),
        ),
    ]