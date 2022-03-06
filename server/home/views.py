from unicodedata import name
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.conf import settings
from .model_control import ModelControl

def index(request):
    if request.user.is_authenticated:

        mc = ModelControl()
        mc.page_start()

        context = {
            'f30': mc.place[0],
            'f31': mc.place[1],
            'f32': mc.place[2]
        }
        return render(request, 'home/home_logged.html', context=context)
    else:
        return render(request, 'home/home_not_logged.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
# Create your views here.
