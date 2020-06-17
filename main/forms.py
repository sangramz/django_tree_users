from django.forms import ModelForm
from .models import Reseller, Customer

class ResellerForm(ModelForm):
    class Meta:
        model = Reseller
        fields = "__all__"
        exclude = ['user']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ['user']