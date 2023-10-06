from rest_framework.viewsets import ReadOnlyModelViewSet

from user_services.models import Subscription
from user_services.serializers import SubscriptionSerializer


class SubscriptionViewSet(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().select_related('plan', 'client', 'client__user').only(
        'client__user__email',
        'client__company_name',
        'plan_id',
    )
    serializer_class = SubscriptionSerializer
