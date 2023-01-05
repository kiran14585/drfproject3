from django.db import models

# Create your models here.

class profile(models.Model):
    

    def nameFile(instance, filename):
     return '/'.join(['images', str(instance.name), filename])


    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="nameFile",blank = True)
