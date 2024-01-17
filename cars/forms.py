from .models import Car
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('description', 'make', 'model', 'year', 'mileage', 'image')




class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',)