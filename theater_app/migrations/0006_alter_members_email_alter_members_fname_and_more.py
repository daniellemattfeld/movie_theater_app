# Generated by Django 5.1.4 on 2024-12-18 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater_app', '0005_alter_members_email_alter_members_fname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='members',
            name='fname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='members',
            name='lname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='members',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
    ]
