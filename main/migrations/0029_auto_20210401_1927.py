# Generated by Django 3.1.4 on 2021-04-01 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20210401_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exntend_user_details',
            name='address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='exntend_user_details',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='exntend_user_details',
            name='mobile_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='exntend_user_details',
            name='pincode',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='exntend_user_details',
            name='role',
            field=models.CharField(blank=True, choices=[('user', 'user'), ('agent', 'agent')], default='user', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='exntend_user_details',
            name='xender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6, null=True),
        ),
    ]
