import random

from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from .models import Place, WishlistAndVisitedPlace, OurRecom, Experience

class ModelControl():
    def __init__(self, user) -> None:
        self.place = []
        self.wish = []
        self.ourr = []
        self.list_v = []
        self.list_w = []
        self.exp = []
        self.user = user

    def page_start(self):
        #for main 3 slots
        a = [(place) for place in Place.objects.all()]
        try:
            x = WishlistAndVisitedPlace.objects.get(user=self.user)
        except ObjectDoesNotExist:
            x = WishlistAndVisitedPlace(user=self.user, wishlist="[]", visited_places="[]", added_date=timezone.now())
            x.save()
            x = WishlistAndVisitedPlace.objects.get(user=self.user)
        list_v = eval(x.visited_places)
        list_w = eval(x.wishlist)
        list_v = list(dict.fromkeys(list_v))
        list_w = list(dict.fromkeys(list_w))
        if len(a) - len(list_v) - len(list_w) < 4 :
            pass
        else:
            for item in list_v:
                a.remove(Place.objects.get(name=item))
            for item in list_w:
                try:
                    a.remove(Place.objects.get(name=item))
                except ValueError:
                    pass
        
        self.place = random.sample(a, 3)

        #for wishlist slots
        for i in list_w:
            self.wish.append(Place.objects.get(name=i))
        self.wish.reverse()
        
        #recomendation
        ourr = OurRecom.objects.all()
        ourr.reverse()
        self.ourr = ourr

        #experiences
        exp = [(exp) for exp in Experience.objects.all()]
        self.exp = exp

    def add_to_wishlist(self, wishname):
         
        x = WishlistAndVisitedPlace.objects.get(user=self.user)
        list = eval(x.wishlist)
        list.append(wishname)
        x.wishlist = list 
        x.save()

        print('clicked')

    def add_to_visited(self, visitname):
        x = WishlistAndVisitedPlace.objects.get(user=self.user)
        list_w = eval(x.wishlist)
        if visitname in list_w:
            list_w.remove(visitname)
            x.wishlist = list_w
        list_v = eval(x.visited_places)
        list_v.append(visitname)
        x.visited_places = list_v
        x.save()

    def visited_places(self):
        x = WishlistAndVisitedPlace.objects.get(user=self.user)
        list_v = eval(x.visited_places)
        list_v = list(dict.fromkeys(list_v))
        list_v.reverse()
        self.list_v = list_v

    def tovisit(self):
        x = WishlistAndVisitedPlace.objects.get(user=self.user)
        list_w = eval(x.wishlist)
        list_w = list(dict.fromkeys(list_w))
        list_w.reverse()
        self.list_w = list_w



        '''self.place = [
            Place.objects.get(name="Sigiriya"),
            Place.objects.get(name="Sigiriya"),
            Place.objects.get(name="Sigiriya")
        ]'''
