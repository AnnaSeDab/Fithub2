from django.db import models


class Gym(models.Model):
    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    website_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
