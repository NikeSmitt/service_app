from celery import shared_task

from django.apps import apps


@shared_task
def update_price(instance_name, instance_id):
    model = apps.get_model('user_services', instance_name)
    print(f'Model found >>> {model}')
    print(f'Instance id >>> {instance_id}')
    subscriptions = model.objects.prefetch_related('subscriptions').get(id=instance_id).subscriptions.all()
    print(f'subs >>> {subscriptions}')
    for subscription in subscriptions:
        subscription.price = (
                subscription.service.full_price - subscription.service.full_price * subscription.plan.discount_percent / 100)
        subscription.save()
