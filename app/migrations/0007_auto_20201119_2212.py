# Generated by Django 3.1.3 on 2020-11-19 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201119_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='topic_id',
            new_name='topic',
        ),
    ]