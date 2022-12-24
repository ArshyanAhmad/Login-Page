from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    number = models.CharField(max_length=12)
    desc = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name