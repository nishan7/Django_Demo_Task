# Generated by Django 3.1.3 on 2020-11-18 18:56

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('nameSlug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('class_num', models.CharField(max_length=255)),
                ('image', stdimage.models.JPEGField(upload_to='')),
            ],
        ),
    ]
