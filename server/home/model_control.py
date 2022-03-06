import random

from .models import Place

class ModelControl():
    def __init__(self) -> None:
        self.place = []
    def page_start(self):
        a = set(Place.objects.all())
        self.place = random.sample(list(a), 3)



        '''self.place = [
            Place.objects.get(name="Sigiriya"),
            Place.objects.get(name="Sigiriya"),
            Place.objects.get(name="Sigiriya")
        ]'''
