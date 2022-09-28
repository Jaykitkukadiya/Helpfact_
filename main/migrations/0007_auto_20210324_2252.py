# Generated by Django 3.1.4 on 2021-03-24 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_task_notification_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completed_task',
            name='task_detail_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.task_detail', unique=True),
        ),
        migrations.AlterField(
            model_name='panding_task',
            name='task_detail_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.task_detail', unique=True),
        ),
        migrations.AlterField(
            model_name='payment_info',
            name='task_detail_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.task_detail', unique=True),
        ),
    ]