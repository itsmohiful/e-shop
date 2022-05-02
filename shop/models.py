import uuid
from typing import OrderedDict

from accounts.models import Customer
from django.db import models
from django.forms import DateTimeField, IntegerField


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True,null=True,blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    discount_price = models.DecimalField(max_digits=6,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    

    def __str__(self):
        return self.name



class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_complete = models.BooleanField(default=False)
    placed_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return str(self.id)
    

    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        return sum([item.quantity for item in orderitems])


class OrderItem(models.Model):
    quantity = models.IntegerField(default=0)
    placed_at = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Order Items'


    @property
    def get_total(self):
        return self.product.discount_price * self.quantity
