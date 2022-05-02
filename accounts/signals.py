from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Customer


#autometic create customer profile
@receiver(post_save, sender=User)
def create_customer(sender,instance,created,**kwargs):
    #print(f'create customer er {sender, instance, created}')
    if created:
        Customer.objects.create(user=instance)


#update customer profile
@receiver(post_save, sender=Customer)
def update_customer(sender,instance,created,**kwargs):
    #print(f'update customer er {sender, instance}')
    if not created:
        customer = instance
        user = customer.user
        user.name = customer.name
        user.save()



# #delete customer profile
# @receiver(post_delete, sender=Customer)
# def delete_customer(sender, instance, created, **kwargs):
#     if not created:
#         user = instance.user
#         user.delete()
