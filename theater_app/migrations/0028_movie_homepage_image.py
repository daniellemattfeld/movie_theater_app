# Generated by Django 5.1.4 on 2025-02-15 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0027_showtime_tickets_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='homepage_image',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
