from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.conf import settings
from .model_control import ModelControl

def index(request):
    if request.user.is_authenticated:

        mc = ModelControl(request.user)
        mc.page_start()

        context = {
            'f30': mc.place[0],
            'f31': mc.place[1],
            'f32': mc.place[2],
            'or0': mc.ourr[0],
            'or1': mc.ourr[1],
            'or2': mc.ourr[2],
            'or3': mc.ourr[3],
            'or4': mc.ourr[4],
            'or5': mc.ourr[5],
        }
        
        for item in mc.wish:
            context[f'w{mc.wish.index(item)}'] = mc.wish[mc.wish.index(item)]
        
        for item in mc.exp:
            context[f'exp{mc.exp.index(item)}'] = mc.exp[mc.exp.index(item)]

        if (request.POST.get('addtw')):
            mc.add_to_wishlist(request.POST.get('addtw'))
            print(f"\"{request.POST.get('addtw')}\" Added to the Wishlists")

        if (request.POST.get('visited')):
            mc.add_to_visited(request.POST.get('visited'))
            print(f"\"{request.POST.get('visited')}\" Added to the Visited Places")

        return render(request, 'home/home_logged.html', context=context)
    else:
        return render(request, 'home/home_not_logged.html')

def visited_places(request):
    if request.user.is_authenticated:
        mc = ModelControl(request.user)
        mc.visited_places()

        context = {}
        for item in mc.list_v:
            context[f'vp{mc.list_v.index(item)}'] = mc.list_v[mc.list_v.index(item)]
            pass
        return render(request, 'home/visited_places.html', context=context)

def wishlist(request):
    if request.user.is_authenticated:
        mc = ModelControl(request.user)
        mc.tovisit()

        context = {}
        for item in mc.list_w:
            context[f'wp{mc.list_w.index(item)}'] = mc.list_w[mc.list_w.index(item)]
        
        if (request.POST.get('visited')):
            mc.add_to_visited(request.POST.get('visited'))
            print(f"\"{request.POST.get('visited')}\" Added to the Visited Places")

        return render(request, 'home/wishlist.html', context=context)

def about_us(request):
    return render(request, 'home/about_us.html')

def contact_us(request,):
    return render(request, 'home/contact_us.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
# Create your views here.
