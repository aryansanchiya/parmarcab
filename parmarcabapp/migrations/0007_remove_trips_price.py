# Generated by Django 5.0.7 on 2024-07-24 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parmarcabapp', '0006_trips'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trips',
            name='price',
        ),
    ]
