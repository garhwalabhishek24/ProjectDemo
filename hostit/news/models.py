from django.db import models
from tinymce.models import HTMLField
class news(models.Model):
    tittle = models.CharField(max_length=100)
    newdesc = HTMLField()


# Create your models here.
