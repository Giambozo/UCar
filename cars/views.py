from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class CarPageView(TemplateView):
    template_name = 'cars/cars.html'