# Generated by Django 5.1.4 on 2025-02-07 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0011_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='movie_images/'),
        ),
    ]
