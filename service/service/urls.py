from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user_services.views import SubscriptionViewSet

router = DefaultRouter()
router.register('api/subscriptions', SubscriptionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

