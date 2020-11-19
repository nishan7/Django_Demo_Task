from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from django.utils import timezone
from django.views.generic import ListView, DetailView

from app.models import Topic, Subscription


class TopicView(DetailView):
    """
    Renders page page that provides detail info about the project
    """
    template_name = "app/detail.html"
    model = Topic

class HomeView(ListView):
    """
    Responsible for the Main Home view of the website
    It currently has a option to search
    """
    paginate_by = 5
    template_name = "app/home.html"

    def get_queryset(self):
        """
        Return the list of items for this view.

        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        if 'search' in self.request.GET:
            return Topic.objects.filter(name__contains=self.request.GET['search'])
        else:
            return Topic.objects.all()



def subscribe(request, topic_id):
    """
    Subscribes a user to a specific topic/tutorial
    """
    topic = Topic.objects.get(id=topic_id)
    if not Subscription.objects.filter(topic=topic, user=request.user).exists():
        new_subscription = Subscription(
                topic=topic,
                user=request.user,
                subscription_date=timezone.now(),
            )
        new_subscription.save()
        messages.success(request, f"{topic.name} has been subscribed.")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', ))

def unsubscribe(request, topic_id):
    """
    Unsubscribes a user to a specific topic/tutorial
    """
    topic = Topic.objects.get(id=topic_id)

    subs = Subscription.objects.get(topic=topic, user=request.user)
    name = subs.topic.name
    subs.delete()
    messages.warning(request, f"{name} has been unsubscribed.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', ))


