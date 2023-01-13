from django.db import models

class Requester(models.Model):
    ASSET_TYPE = (
        ('LAPTOP','LAPTOP'),
        ('TRAVEL_BAG','TRAVEL_BAG'),
        ('PACKAGE','PACKAGE')
    )
    SENSITIVITIES = (
        ('HIGHLY_SENSITIVE','HIGHLY_SENSITIVE'),
        ('SENSITIVE','SENSITIVE'),
        ('NORMAL','NORMAL')
    )
    from_location = models.CharField(max_length=100, primary_key=True)
    to_location = models.CharField(max_length=100)
    date = models.DateField(blank=True)
    assets = models.IntegerField(default=0, verbose_name='No of assets')
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPE)
    sensitivities = models.CharField(max_length=20, choices=SENSITIVITIES)
    recipient = models.CharField(max_length=100)
# Create your models here.
