# Generated by Django 5.1.4 on 2025-02-07 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0017_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
