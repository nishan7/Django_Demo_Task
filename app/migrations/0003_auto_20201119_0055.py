# Generated by Django 3.1.3 on 2020-11-18 19:10

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_topic_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='image',
            field=stdimage.models.JPEGField(default=False, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='id',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
