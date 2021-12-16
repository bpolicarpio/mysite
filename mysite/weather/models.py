from django.db import models

# Create your models here.

class Weather(models.Model):
    weather = models.BooleanField()
    feeling = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.date}"