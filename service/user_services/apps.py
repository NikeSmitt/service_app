from django.apps import AppConfig
from django.db.models.signals import post_save, post_delete


class UserServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_services'
    
    def ready(self):
        from . import signals
        
        
        PlanModel = self.get_model('Plan')
        ServiceModel = self.get_model('Service')
        SubscriptionModel = self.get_model('Subscription')

        post_delete.connect(signals.reset_total_price_cache, sender='user_services.Subscription')
        post_save.connect(signals.update_subscription_price, sender='user_services.Plan')
        post_save.connect(signals.update_subscription_price, sender='user_services.Service')
        post_save.connect(signals.reset_total_price_cache, sender='user_services.Subscription')

        
        
        
        
