from django.apps import AppConfig
from django.db.models.signals import post_save


class UserServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_services'
    
    def ready(self):
        
        from . import signals
        PlanModels = self.get_model('Plan')
        ServiceModels = self.get_model('Service')
        post_save.connect(signals.update_subscription_price, sender='user_services.Plan')
        post_save.connect(signals.update_subscription_price, sender='user_services.Service')
        
        
        
