from django.contrib import admin
from home.models import Place, WishlistAndVisitedPlace, OurRecom, Experience


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass

@admin.register(WishlistAndVisitedPlace)
class WishlistAndVisitedPlaceAdmin(admin.ModelAdmin):
    pass

@admin.register(OurRecom)
class OurRecomAdmin(admin.ModelAdmin):
    pass

@admin.register(Experience)
class Experience(admin.ModelAdmin):
    pass

# Register your models here.
