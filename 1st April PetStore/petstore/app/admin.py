from django.contrib import admin
from .models import Pet
# Register your models here.

class PetAdmin(admin.ModelAdmin):
    list_display=[
        'petid',
        'petname',
        'userid' ,
        'age' ,
        'gender' , 
        'description' ,
        'photo' 
    ]

admin.site.register(Pet,PetAdmin)
