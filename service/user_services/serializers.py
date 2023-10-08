from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from user_services.models import Subscription, Plan, Service


class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class SubscriptionSerializer(ModelSerializer):
    plan = PlanSerializer()
    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.user.email')
    price = serializers.CharField()
    service = ServiceSerializer()
    
    class Meta:
        model = Subscription
        fields = ['id', 'plan_id', 'service', 'client_name', 'email', 'plan', 'price']
