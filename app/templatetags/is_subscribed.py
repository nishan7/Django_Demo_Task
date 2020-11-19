from django import template

from app.models import Subscription

register = template.Library()


@register.simple_tag
def is_subscribed(user, tutorial):
    """
    Check weather a user is been subscribed to a tutorial/Topic or not
    :param user: Student
    :param tutorial: Tutorial/Topic
    :return: Boolean
    """
    if user.is_authenticated:
        qs = Subscription.objects.filter(user=user, topic_id=tutorial)
        if qs.exists():
            return True
    return False
