from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CarForm
from .models import Car
from .forms import RegisterUserForm

def bmw_page(request):
    return render(request, 'BMW.html')

def mers_page(request):
    return render(request, 'Mercedes-Benz.html')

def volks_page(request):
    return render(request, 'Volkswagen.html')

def ford_page(request):
    return render(request, 'Ford.html')

def audi_page(request):
    return render(request, 'audi.html')

def sko_page(request):
    return render(request, 'Skoda.html')

def niss_page(request):
    return render(request, 'Nissan.html')

def toyo_page(request):
    return render(request, 'Toyota.html')

def hyu_page(request):
    return render(request, 'Hyundai.html')

def hon_page(request):
    return render(request, 'Honda.html')

def chev_page(request):
    return render(request, 'Chevrolet.html')

def maz_page(request):
    return render(request, 'Mazda.html')

def cit_page(request):
    return render(request, 'Citroen.html')

def vol_page(request):
    return render(request, 'Volvo.html')

def fiat_page(request):
    return render(request, 'Fiat.html')

def lex_page(request):
    return render(request, 'Lexus.html')
def ren_page(request):
    return render(request, 'Renault.html')

def jeep_page(request):
    return render(request, 'Jeep.html')


def lr_page(request):
    return render(request, 'Land Rover.html')

def che_page(request):
    return render(request, 'Chery.html')

def dac_page(request):
    return render(request, 'Dacia.html')
def my_view(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'my_template.html', context)

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(pk=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})

def AfterButton_page(request):
    return render(request, 'AfterButtonCar.html')

def Obrob_page(request):
    return render(request, 'ObrabotkaDannih.html')

def CarForm_page(request):
    return render(request, 'car_form.html')



def car_form(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CarForm()

    return render(request, 'car_form.html', {'form': form})


def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars:car_list')  #
    else:
        form = CarForm()

    return render(request, 'car_form.html', {'form': form})


class DataMixin:
    def get_user_context(self, title):
        context = {
            'user_title': title,
        }
        return context

class registration_view(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'registration_page.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Registration')
        return {**context, **c_def}


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))



class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'car_form.html'
    success_url = '/cars/car/list/'

    def form_valid(self, form):
        return super().form_valid(form)


def login_page(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('cars/login')