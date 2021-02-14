from django.db import models


# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/&d')
    desc = models.TextField(blank=True, verbose_name='Description')
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    is_mvp = models.BooleanField(default=False)
    message = models.CharField(max_length=200)
    contact_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-contact_date']