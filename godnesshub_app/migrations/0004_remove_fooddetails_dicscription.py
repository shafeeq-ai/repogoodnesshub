# Generated by Django 5.1.3 on 2024-12-07 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('godnesshub_app', '0003_fooddetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooddetails',
            name='dicscription',
        ),
    ]
