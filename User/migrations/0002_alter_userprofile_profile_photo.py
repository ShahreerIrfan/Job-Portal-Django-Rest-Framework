# Generated by Django 5.0.1 on 2024-05-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("User", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_photo",
            field=models.ImageField(null=True, upload_to="User/images/profile_photo"),
        ),
    ]
