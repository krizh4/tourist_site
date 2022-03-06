from django.contrib import admin
from home.models import Place, VisitedPlace, Wishlist


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass

@admin.register(VisitedPlace)
class VisitedPlaceAdmin(admin.ModelAdmin):
    pass

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    pass

# Register your models here.
