# Generated by Django 5.1.7 on 2025-03-20 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="photo",
            field=models.ImageField(default=None, null=True, upload_to="images"),
        ),
    ]
