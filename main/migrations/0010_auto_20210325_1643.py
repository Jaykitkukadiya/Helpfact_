# Generated by Django 3.1.4 on 2021-03-25 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210325_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='deadline',
            field=models.CharField(max_length=500),
        ),
    ]