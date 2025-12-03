from django.db import models
from django.utils import timezone
from datetime import timedelta
from .client import Client
from .insurence_type import InsurenceType

class Subscription(models.Model):
    payment_method = models.CharField(max_length=100, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    insurence = models.ForeignKey(InsurenceType, on_delete=models.CASCADE)
    valid_till = models.DateTimeField(null=True, blank=True)
    starts_at = models.DateTimeField(null=True,blank=True)
    
    
    def save(self,*args, **kwargs):
        self.valid_till = self.starts_at+timedelta(days=self.insurence.expires_in_days)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.client.name} — valid till: {self.valid_till.date()}"

    @property
    def is_expired(self):
        return self.valid_till > timezone.now()
    
    @property
    def days_left(self):
        delta = self.valid_till - timezone.now()
        return max(delta.days,0)
    
    @days_left.setter
    def days_left(self, value):
        if isinstance(value, timedelta):
            self.valid_till = timezone.now() + value
        else:
            raise ValueError("days_left must be a timedelta")