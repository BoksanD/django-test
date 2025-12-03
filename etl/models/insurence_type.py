from django.db import models

class InsurenceType(models.Model):
    name = models.CharField(max_length=50,null=False)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    expires_in_days = models.IntegerField(default=30)

    def __str__(self):
        return f'{self.name} - is valid for {self.expires_in_days} day(s)'