# Generated by Django 4.1.2 on 2022-10-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_from',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_to',
            field=models.DateField(),
        ),
    ]
