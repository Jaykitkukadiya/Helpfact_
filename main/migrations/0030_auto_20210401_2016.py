# Generated by Django 3.1.4 on 2021-04-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20210401_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_info',
            name='agent_payment_cause',
            field=models.CharField(default='...', max_length=500),
        ),
        migrations.AddField(
            model_name='payment_info',
            name='user_payment_cause',
            field=models.CharField(default='...', max_length=500),
        ),
    ]
