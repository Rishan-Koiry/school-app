# Generated by Django 5.1.7 on 2025-03-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_alter_userinfo_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='address',
            field=models.TextField(default='Not provided'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='dob',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='documents',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='parent_email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='parent_name',
            field=models.CharField(default='Not provided', max_length=100),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='parent_phone',
            field=models.CharField(default='000-000-0000', max_length=15),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(default='000-000-0000', max_length=15),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='previous_school',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='terms',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='class_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='roll',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
