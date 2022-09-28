# Generated by Django 3.1.4 on 2021-03-24 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_delete_temp_task_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completed_task',
            name='status',
            field=models.CharField(choices=[('success', 'success'), ('fail', 'fail')], default='success', max_length=8),
        ),
        migrations.AlterField(
            model_name='exntend_user_details',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('agent', 'agent')], default='user', max_length=6),
        ),
        migrations.AlterField(
            model_name='panding_task',
            name='status',
            field=models.CharField(choices=[('initilize', 'initilize'), ('accepted', 'accepted')], default='initilize', max_length=10),
        ),
        migrations.AlterField(
            model_name='payment_info',
            name='agent_payment_status',
            field=models.CharField(choices=[('success', 'success'), ('fail', 'fail')], default='fail', max_length=8),
        ),
        migrations.AlterField(
            model_name='payment_info',
            name='user_payment_status',
            field=models.CharField(choices=[('success', 'success'), ('fail', 'fail')], default='fail', max_length=8),
        ),
    ]