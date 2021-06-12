from django import forms
from django.db import models

from  .models import Product

class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'Name',
            'Email_id',
            'Phone_number',
            'Image'

        ]