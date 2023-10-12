import sys

from django.conf import settings
from django.core.cache import cache

from tasks import update_price


def update_subscription_price(sender, **kwargs):
    updated_fields = kwargs.get('update_fields')
    checked_fields = ['full_price', 'discount_percent']
    if updated_fields is not None and is_field_accepted(checked_fields, updated_fields):
        instance = kwargs.get('instance')
        update_price.delay(instance.__class__.__name__, instance.id)
        
        
def is_field_accepted(checked_fields: [str], updated_fields: [str]):
    for field in updated_fields:
        if field in checked_fields:
            return True
    return False


def reset_total_price_cache(sender, **kwargs):
    cache.delete(settings.PRICE_CACHE_NAME)
