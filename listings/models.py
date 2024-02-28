from django.db import models

class House(models.Model):
    STATUS_CHOICES = (
        ('rent', 'For Rent'),
        ('sale', 'For Sale'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    image = models.ImageField(upload_to='images/')
    image_url = models.URLField(blank=True)  # Field to store the URL of the image in S3
   

    def save(self, *args, **kwargs):
        if self.image:
            self.image_url = self.image.url
        super().save(*args, **kwargs)
