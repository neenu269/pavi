# Generated by Django 4.1.3 on 2023-06-29 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='date',
        ),
    ]
