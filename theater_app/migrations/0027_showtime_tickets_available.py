# Generated by Django 5.1.4 on 2025-02-14 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0026_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='showtime',
            name='tickets_available',
            field=models.IntegerField(default=30),
        ),
    ]
