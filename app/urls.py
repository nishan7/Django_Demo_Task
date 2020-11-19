from django.urls import path

from app.views import *

app_name = 'app'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('detail/<slug:slug>/', TopicView.as_view(), name='detail'),
    path('subscribe/<topic_id>', subscribe, name='subscribe'),
    path('unsubscribe/<topic_id>', unsubscribe, name='unsubscribe'),

]
