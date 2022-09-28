# Generated by Django 3.1.4 on 2021-03-28 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0022_delete_online'),
    ]

    operations = [
        migrations.CreateModel(
            name='online',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=400)),
                ('state', models.CharField(choices=[('user', 'user'), ('agent', 'agent')], default='user', max_length=6)),
                ('socket_name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]