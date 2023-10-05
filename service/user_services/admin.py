from django.contrib import admin
from user_services.models import Service, Subscription, Plan

admin.site.register(Service)
admin.site.register(Subscription)
admin.site.register(Plan)
