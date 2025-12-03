from django.contrib import admin

from .models import Client,InsurenceType,Subscription

admin.site.register(Client)
admin.site.register(InsurenceType)
admin.site.register(Subscription)
