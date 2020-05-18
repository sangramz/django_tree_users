from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Reseller, Customer

# Register your models here.
admin.site.register(Reseller, MPTTModelAdmin)
admin.site.register(Customer)
