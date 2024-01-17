from django.db import models
from django.contrib.auth.models import AbstractUser

class Car(models.Model):
    description = models.TextField('Описание')
    make = models.CharField('Марка', max_length=50)
    model = models.CharField('Модель', max_length=50)
    year = models.IntegerField(default=0)
    mileage = models.IntegerField(default=0)
    image = models.ImageField(upload_to='car_images', default='default_image.jpg')

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'



from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext as _

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
        related_name='customuser_groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='customuser_permissions',
    )

    def __str__(self):
        return self.username
