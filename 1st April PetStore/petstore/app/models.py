from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pet(models.Model):
    petid = models.PositiveBigIntegerField(primary_key=True)
    petname = models.CharField(max_length=100, null=True, default=None)
    userid = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    age = models.PositiveBigIntegerField()
    type = (("Male", "Male"), ("Female", "Female"))
    gender = models.CharField(max_length=20, choices=type)
    description = models.TextField()
    photo = models.ImageField(upload_to="images")