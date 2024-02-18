# Generated by Django 4.2.10 on 2024-02-16 18:23

import django.core.validators
from django.db import migrations, models
import petstagram.photos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='pet_photos/', validators=[petstagram.photos.models.MaxFileSizeValidator(limit_value=5242880)])),
                ('description', models.TextField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('pets', models.ManyToManyField(to='pets.pet')),
            ],
        ),
    ]
