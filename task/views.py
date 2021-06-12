from django.shortcuts import render
from .forms import Productform
from .models import Product

# Create your views here.

def Product_view(request):
    form = Productform(request.POST or None)
    if form.is_valid():
        form.save()


    context = {'form' : form}


    return render(request, 'task/detail.html',context)