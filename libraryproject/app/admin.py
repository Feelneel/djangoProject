from django.contrib import admin
from .models import Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display=[
    "isbn",
    "title",
    "author",
    "category",
    "price",
    "qty",
    "dop",
    "description",
    "photo"
    ]

admin.site.register(Book,BookAdmin)