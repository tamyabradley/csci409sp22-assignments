# Generated by Django 4.0.2 on 2022-02-07 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_people', models.IntegerField()),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flights')),
            ],
        ),
    ]
