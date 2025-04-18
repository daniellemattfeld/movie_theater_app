# Generated by Django 5.1.4 on 2024-12-18 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0002_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='email',
            field=models.EmailField(default='EMAIL', max_length=100),
        ),
        migrations.AddField(
            model_name='members',
            name='fname',
            field=models.CharField(default='<FNAME>', max_length=100),
        ),
        migrations.AddField(
            model_name='members',
            name='lname',
            field=models.CharField(default='<LNAME>', max_length=100),
        ),
        migrations.AlterField(
            model_name='members',
            name='password',
            field=models.CharField(default='<PASSWORD>', max_length=50),
        ),
    ]
