# Generated by Django 4.1.4 on 2023-05-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_profile_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_pic",
            field=models.ImageField(upload_to="pp"),
        ),
    ]
