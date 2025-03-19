from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.PositiveIntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    emailid=models.EmailField(max_length=20)