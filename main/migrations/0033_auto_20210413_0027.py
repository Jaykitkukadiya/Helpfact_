# Generated by Django 3.1.4 on 2021-04-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20210413_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='document',
            field=models.FileField(blank=True, default='profile/defaultprofile.png', null=True, upload_to='task/document/'),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='proof',
            field=models.FileField(blank=True, default='profile/defaultprofile.png', null=True, upload_to='task/proof/'),
        ),
    ]