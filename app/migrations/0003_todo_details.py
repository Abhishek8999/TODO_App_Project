# Generated by Django 4.1.2 on 2022-10-05 10:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_todo_date_from_alter_todo_date_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='details',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
