from django.contrib import admin

from user_services.models import Service, Subscription, Plan

admin.site.register(Subscription)


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        
        updated_fields = []
        if change:
            if form.initial['discount_percent'] != form.cleaned_data['discount_percent']:
                updated_fields.append('discount_percent')
        obj.save(update_fields=updated_fields)
        
        
@admin.register(Service)
class PlanService(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        updated_fields = []
        field_name = 'full_price'
        if change:
            if form.initial[field_name] != form.cleaned_data[field_name]:
                updated_fields.append(field_name)
        obj.save(update_fields=updated_fields)
        
