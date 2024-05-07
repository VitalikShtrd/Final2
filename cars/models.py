from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _

class Car(models.Model):
    description = models.TextField('Описание')
    make = models.CharField('Марка', max_length=50)
    model = models.CharField('Модель', max_length=50)
    year = models.IntegerField(default=0)
    mileage = models.IntegerField(default=0)
    image = models.ImageField(upload_to='car_images', default='default_image.jpg')

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'

class VehicleBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarInfo(models.Model):
    brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    mileage = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.brand.name} {self.model} ({self.year})"

class CarDetail(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    vin = models.CharField(max_length=17, unique=True)

    def __str__(self):
        return f"Details for {self.car.make} {self.car.model} ({self.car.year})"

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='custom_user_groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_user_permissions',
    )

    def __str__(self):
        return self.username


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']