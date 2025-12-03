from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255, null=False)
    reg_date = models.DateTimeField("register date")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name