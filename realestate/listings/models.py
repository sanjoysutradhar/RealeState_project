from django.db import models
from realtors.models import Realtor
from django.contrib.auth.models import User


# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.BooleanField()
    sqFeet = models.IntegerField()
    lot_size = models.DecimalField(decimal_places=2, max_digits=5)
    is_published = models.BooleanField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d')
    list_date = models.DateTimeField(auto_now_add=False)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-list_date",)


class Inquiry(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=150)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ("-timestamp",)
        verbose_name = 'Inquiry'
        verbose_name_plural = 'Inquires'
