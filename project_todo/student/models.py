from django.db import models

# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=200)
    Email=models.EmailField(max_length=254)
    Phone=models.CharField(max_length=50)

    def __str__(self) :
        return self.Name
