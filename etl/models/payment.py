from django.db import models
from .subscription import Subscription

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    paid_at = models.DateField(null=False)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subscription.name} is paid at {self.paid_at}'