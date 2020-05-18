from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Reseller(MPTTModel):
    reseller_name = models.CharField(max_length=40)
    reseller_email = models.EmailField(max_length=70,blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['reseller_name']

    def __str__(self):
        return self.reseller_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=40)
    customer_email = models.EmailField(max_length=70,blank=True)
    reseller = models.ForeignKey(Reseller, on_delete=models.CASCADE, null=True, blank=True, related_name='cust_children')

    def __str__(self):
        return self.customer_name