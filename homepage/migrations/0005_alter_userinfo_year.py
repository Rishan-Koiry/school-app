# Generated by Django 5.1.7 on 2025-03-20 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_userinfo_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='year',
            field=models.IntegerField(default=2023),
        ),
    ]
