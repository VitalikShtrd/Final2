# Generated by Django 4.2.6 on 2024-01-10 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car1_remove_car_price_car_image_car_mileage_car_year_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Car1',
        ),
    ]
