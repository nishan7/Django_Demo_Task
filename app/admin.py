from django.contrib import admin

# Register your models here.
from app.models import Topic, Subscription

admin.site.register(Topic)
admin.site.register(Subscription)
