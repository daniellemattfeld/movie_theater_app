# Generated by Django 5.1.4 on 2025-02-07 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0015_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
