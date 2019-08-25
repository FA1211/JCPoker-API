# Generated by Django 2.2.4 on 2019-08-25 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jesuspokerapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='players',
        ),
        migrations.AlterField(
            model_name='sessionresult',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='jesuspokerapi.Session'),
        ),
    ]