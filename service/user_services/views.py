from django.conf import settings
from django.core.cache import cache
from django.db.models import F
from django.db.models import Sum
from rest_framework.viewsets import ReadOnlyModelViewSet

from user_services.models import Subscription
from user_services.serializers import SubscriptionSerializer


class SubscriptionViewSet(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().select_related('service', 'plan', 'client', 'client__user').only(
        'client__user__email',
        'client__company_name',
        'service',
        'plan',
        'price',
    )
    serializer_class = SubscriptionSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)
        
        total_price_cache = cache.get(settings.PRICE_CACHE_NAME)
        
        if total_price_cache is not None:
            total_price = total_price_cache
        else:
            total_price = queryset.aggregate(total=Sum('price')).get('total')
            cache.set(settings.PRICE_CACHE_NAME, total_price, 30)
        
        response_data = {
            'subscription': response.data,
            'total_amount': total_price
        }
        response.data = response_data
        return response
    
    
