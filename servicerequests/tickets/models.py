from django.db import models

# Create your models here.
class Ticket(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    reported_by = models.TextField(null=True, blank=True)
    assigned_to = models.TextField(null=True, blank=True)
    status = models.CharField(null=True,max_length=30)
