# Generated by Django 4.1.2 on 2022-10-05 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_todo_date_from_alter_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_from',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_to',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=25),
        ),
    ]
