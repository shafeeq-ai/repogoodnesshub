# Generated by Django 5.1.3 on 2024-11-19 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('godnesshub_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CampRegistrationTable',
            new_name='CampTable',
        ),
        migrations.AlterField(
            model_name='managetable',
            name='Phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resturanttable',
            name='Phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
