from django.db import models


# Create your models here.

class photo_upload(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to ='first/')

