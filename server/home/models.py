from django.db import models

from django.contrib.auth.models import User

class Place(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(max_length=200)
    description = models.TextField()
    location = models.URLField(max_length=200)

    class Meta():
        ordering = ('name',)
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __str__(self):
        return (self.name)

class VisitedPlace(models.Model):
    visited_places = models.TextField()
    added_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

    class Meta():
        verbose_name = 'Visited Place'
        verbose_name_plural = 'Visited Places'

    def __str__(self):
        return (self.user.username)

class Wishlist(models.Model):
    to_visit = models.TextField()
    added_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'
    
    def __str__(self):
        return (self.user.username)


# Create your models here.
