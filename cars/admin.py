
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Car

admin.site.register(Car)

User = get_user_model()
admin.site.unregister(User)
admin.site.register(User)
