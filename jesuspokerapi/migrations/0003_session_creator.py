# Generated by Django 2.2.4 on 2019-08-30 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jesuspokerapi', '0002_auto_20190828_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_sessions', to=settings.AUTH_USER_MODEL),
        ),
    ]
