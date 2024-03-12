from django.http import request
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import cars
from cars.models import Car
from pages.views import HomePageView


# Create your views here.

class CarPageView(TemplateView):
    template_name = 'cars/cars.html'


class CarSinglePageView(DetailView):
    model = Car
    template_name = 'cars/cars_detail.html'


class CarsPageView(ListView):
    template_name = 'cars/cars.html'
    # paginator = Paginator(cars, 2)  # <!--                       AICI             -->
    model = Car


    def get_context_data(self, **kwargs):
        context = super(CarsPageView, self).get_context_data(**kwargs)
        context['all_cars'] = Car.objects.all()
        return context


class SearchView(ListView):
    model = Car
    template_name = 'cars/search.html'

    # if 'keyword' in :?
    # keywod =                                                 <!--                       AICI             -->
    # car = Car.filter(?)

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['all_cars'] = Car.objects.all()
        return context
