from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import Subscription
from django import forms

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['payment_method', 'client', 'insurence', 'starts_at']
        widgets = {
            'starts_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.starts_at:
            self.initial['starts_at'] = self.instance.starts_at.strftime('%Y-%m-%dT%H:%M')
