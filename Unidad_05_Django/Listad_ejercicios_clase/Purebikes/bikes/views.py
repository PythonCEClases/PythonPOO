from django.shortcuts import render
from bikes.models import Bike
from django.db.models import Sum, Count


# Create your views here.

def index(request):
    return render(request, 'index.html')

def all_bikes(request):
    bikes = Bike.objects.all()
    return render(request, 'all_bikes.html', {'bikes': bikes})

def brands(request):
    brands = Bike.objects.values_list('brand', flat=True).distinct().order_by('brand')
    return render(request, 'brands.html', {'brands': brands})

def counter(request):
    group_data = Bike.objects.values_list('brand').annotate(
        counter=Count('id')
    )
    
    return render(request, 'counter_brand.html', {
        'data': group_data,        
    })
