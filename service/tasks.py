import datetime
import time

from celery import shared_task
from celery_singleton import Singleton
from django.apps import apps
from django.db import transaction


@shared_task(base=Singleton)
def update_price(instance_name, instance_id):
    model = apps.get_model('user_services', instance_name)
    
    with transaction.atomic():
        subscriptions = model.objects.select_for_update().prefetch_related('subscriptions').get(
            id=instance_id).subscriptions.all()
        for subscription in subscriptions:
            subscription.price = (
                    subscription.service.full_price - subscription.service.full_price * subscription.plan.discount_percent / 100)
            subscription.save()


# @shared_task(base=Singleton)
# def set_comment(subscription_id):
#     from user_services.models import Subscription
#
#     subscription = Subscription.objects.get(id=subscription_id)
#
#     time.sleep(27)
#
#     subscription.comment = str(datetime.datetime.now())
#     subscription.save()
