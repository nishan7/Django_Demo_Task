from django.conf import settings
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify
from stdimage import JPEGField


class Topic(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    class_num = models.CharField(max_length=255)
    image = JPEGField(upload_to="", variations={
        'thumbnail': {"width": 400, "height": 250, "crop": True}})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Topic, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("app:detail", kwargs={
            'slug': self.slug
        })

    def unsubscribe(self):
        return reverse("app:unsubscribe", kwargs={
            'topic_id': self.id
        })

    def subscribe(self):
        return reverse("app:subscribe", kwargs={
            'topic_id': self.id
        })


class Subscription(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='handyman')
    subscription_date = models.DateTimeField(auto_now_add=True)