from django.db import models

class services(models.Model):
    icon=models.CharField(max_length=50)
    tittle=models.CharField(max_length=50)
    description=models.TextField()
