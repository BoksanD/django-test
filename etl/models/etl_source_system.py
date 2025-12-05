from django.db import models

class EtlSourceSystem(models.Model):

    class SystemTypes(models.IntegerChoices):
        EXCEL = 1, 'Excel'
        CSV   = 2, 'CSV'
        PDF   = 3, 'PDF'

    system_name = models.CharField(max_length=255, null=False)
    system_type = models.IntegerField(choices=SystemTypes.choices, null=False)
    parameters = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.system_name}'
