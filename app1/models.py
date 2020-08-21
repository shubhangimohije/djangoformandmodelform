from django.db import models

# Create your models here.

class Student(models.Model):
    sid=models.IntegerField()
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)

    def __str__(self):
        return self.name


class University(models.Model):
    code=models.IntegerField()
    name=models.CharField(max_length=70)
    city=models.CharField(max_length=70)

    def __str__(self):
        return self.name
