from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView

from cars.models import Car


# Create your views here.

class CarPageView(TemplateView):
    template_name = 'cars/cars.html'


class CarSinglePageView(DetailView):
    model = Car
    template_name = 'cars/cars_detail.html'
