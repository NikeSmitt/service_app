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
        'plan'
    )
    #     .annotate(price=(
    #         F('service__full_price') -
    #         F('service__full_price') * F('plan__discount_percent') / 100.0
    # ))
    serializer_class = SubscriptionSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)
        response_data = {
            'subscription': response.data,
            'total_amount': queryset.aggregate(total=Sum('price')).get('total')}
        response.data = response_data
        return response
    
    
