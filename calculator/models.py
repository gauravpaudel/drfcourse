from django.db import models

class Numeric(models.Model):
    numa = models.FloatField()
    numb = models.FloatField()
    result = models.FloatField(blank = True)