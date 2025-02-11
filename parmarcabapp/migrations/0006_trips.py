# Generated by Django 5.0.7 on 2024-07-24 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parmarcabapp', '0005_alter_cabsonlineform_journey_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('offer', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('sedan', models.IntegerField(null=True)),
                ('suv', models.IntegerField(null=True)),
                ('hatchback', models.IntegerField(null=True)),
                ('xuv', models.IntegerField(null=True)),
                ('luxury', models.IntegerField(null=True)),
            ],
        ),
    ]
