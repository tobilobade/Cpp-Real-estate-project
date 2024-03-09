from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class House(models.Model):
    HOUSE_CHOICES = (
        ('single_family_detached', 'Single-family detached'),
        ('bungalow', 'Bungalow'),
        ('ranch_style', 'Ranch-style'),
        ('cottage', 'Cottage'),
        ('apartment', 'Apartment'),
        ('duplex', 'Duplex'),
        ('triplex', 'Triplex'),
        ('penthouse', 'Penthouse'),
        ('terrace_house', 'Terrace House'),
        ('studio_apartment', 'Studio Apartment'),
        ('semi_detached', 'Semi-detached'),
        ('mansion', 'Mansion'),
    )
    STATUS_CHOICES = (
        ('rent', 'For Rent'),
        ('sale', 'For Sale'),
    )
    title = models.CharField(max_length=100, choices=HOUSE_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    image = models.ImageField(upload_to='images/')
    image_url = models.URLField(blank=True)  # I added this Field to store the URL of the image in S3
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = CountryField(default='Ireland')
   

    def save(self, *args, **kwargs):
        if self.image:
            self.image_url = self.image.url
        super().save(*args, **kwargs)
