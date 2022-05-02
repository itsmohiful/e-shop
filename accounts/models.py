from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to = './customer_profile_photo',
            default = 'default_profile.jpg', null=True, blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)



    def __str__(self):
        return str(self.user)
