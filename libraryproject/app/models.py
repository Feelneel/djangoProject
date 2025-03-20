from django.db import models

# Create your models here.

class Book(models.Model):
    isbn=models.PositiveIntegerField(primary_key=True)
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    type=(('programming','programming'),('database','database'))
    category=models.CharField(max_length=50,choices=type)
    price=models.FloatField()
    qty=models.PositiveBigIntegerField(default=1)
    dop=models.DateField()
    description=models.TextField()
    photo=models.ImageField(upload_to='images',null=True,default=None)
