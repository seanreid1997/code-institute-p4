# Generated by Django 4.1 on 2022-09-14 20:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='https://t3.ftcdn.net/jpg/03/46/83/96/360_    F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg', max_length=255, verbose_name='image'),
        ),
    ]
