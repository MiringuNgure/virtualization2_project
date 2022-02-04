from django.db import models

class Airport_data(models.Model):
    name = models.CharField(max_length=100)
    airport_code = models.CharField(primary_key=True, max_length=100)
    temperature = models.CharField(max_length= 100)
    dewpoint = models.CharField(max_length=200)
    pressure = models.CharField(max_length=200)
    winds = models.CharField(max_length=200)
    visibility = models.CharField(max_length=200)
    ceiling = models.CharField(max_length=200)
    clouds = models.CharField(max_length=200)

    class Meta:
        db_table = "airports"

