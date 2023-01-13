from django.db import models

class Rider(models.Model):
    TRAVEL_MEDIUM = (
        ('BUS', 'BUS'),
        ('CAR', 'CAR'),
        ('TRAIN', 'TRAIN')
    )
    from_location = models.CharField(max_length=100, primary_key=True)
    to_location = models.CharField(max_length=100)
    date = models.DateField()
    travel_medium = models.CharField(max_length=20, choices=TRAVEL_MEDIUM)
    assets_quantity = models.IntegerField(default=0)