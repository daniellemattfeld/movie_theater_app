# Generated by Django 5.1.4 on 2025-02-12 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0021_upcoming'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upcoming',
            name='movie',
        ),
        migrations.AddField(
            model_name='upcoming',
            name='upcoming_movie',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
