from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('tovisit/', views.wishlist, name='tovisit'),
    path('visited/', views.visited_places, name='visited_places'),
    path('contact/', views.contact_us, name='contact_us'),
    path('about/', views.about_us, name='about_us')
]