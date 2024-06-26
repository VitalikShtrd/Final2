# Generated by Django 4.2.6 on 2024-01-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('make', models.CharField(max_length=50, verbose_name='Марка')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('year', models.IntegerField(default=0)),
                ('mileage', models.IntegerField(default=0)),
                ('image', models.ImageField(default='default_image.jpg', upload_to='car_images')),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='price',
        ),
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='car_images'),
        ),
        migrations.AddField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(max_length=50, verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=50, verbose_name='Модель'),
        ),
    ]
