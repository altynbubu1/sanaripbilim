# Generated by Django 5.2 on 2025-04-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_image_course_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='course/'),
        ),
    ]
