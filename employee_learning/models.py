from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return f'{self.id} : {self.name}'

class Division(models.Model):
    div_name=models.CharField(max_length=25)
    def __str__(self):
        return self.div_name