# Generated by Django 4.0.2 on 2022-02-15 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_airline_flights_airline'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='flight_number',
            field=models.IntegerField(default=0),
        ),
    ]