from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True,null=True,blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    discount_price = models.DecimalField(max_digits=6,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
