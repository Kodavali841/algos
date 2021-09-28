from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=200)

class Assignments(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assign = models.CharField(max_length=50)