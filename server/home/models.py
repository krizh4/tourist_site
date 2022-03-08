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

class WishlistAndVisitedPlace(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wishlist = models.TextField(default='[]')
    visited_places = models.TextField(default='[]')
    added_date = models.DateField()

    class Meta():
        verbose_name = 'Wishlist and Visited Place'
        verbose_name_plural = 'Wishlist and Visited Places'

    def __str__(self):
        return (self.user.username)

class OurRecom(models.Model):
    item = models.ForeignKey(Place, on_delete=models.CASCADE)
    added_date = models.DateTimeField()

    class Meta():
        verbose_name = "Our Recommendation"
        verbose_name_plural = "Our Recommendations"
    
    def __str__(self):
        return self.item.name

class Experience(models.Model):
    name = models.TextField(max_length=255)
    link = models.URLField(max_length=250)
    image = models.URLField(max_length=250)

    class Meta():
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
    
    def __str__(self):
        return self.name

# Create your models here.
