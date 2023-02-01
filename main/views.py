from django.shortcuts import render
from main.models import *
# Create your views here.


def CarListView(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'main/car-list.html', context=context)