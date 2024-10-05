from django.db import models
# Create your models here.

class Transfer(models.Model):
    user = models.IntegerField()
    warehouse = models.IntegerField()
    rent_date = models.DateTimeField()
    end_date = models.DateTimeField()
    rent_paid = models.FloatField()
    note = models.TextField(null=True)
    
    def __str__(self):
        return str(self.warehouse)    