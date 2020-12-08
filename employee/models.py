from django.db import models

class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True, blank = True)

