# Generated by Django 3.1.3 on 2020-11-18 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='image',
        ),
    ]
