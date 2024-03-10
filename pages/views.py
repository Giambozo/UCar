from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from cars.models import Car
from pages.models import Team

from .models import Team


# Create your views here.

class HomePageView(ListView):
    model = Team
    template_name = 'pages/home.html'
    # model_search = Car.objects.values_list('model', flat=True).distinct()   <!--          AICI            -->
    # city_search = Car.objects.values_list('city', flat=True).distinct()
    # year_search = Car.objects.values_list('year', flat=True).distinct()
    # body_style_search = Car.objects.values_list('body_style', flat=True).distinct()


    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['featured_cars'] = Car.objects.filter(is_featured=True)
        context['all_cars'] = Car.objects.all()
        return context


class AboutPageView(ListView):
    model = Team
    template_name = 'pages/about.html'


class ServicesPageView(TemplateView):
    template_name = 'pages/services.html'


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

# class CarsPageView(ListView):
#     template_name = 'cars/cars.html'
#     def get_context_data(self, **kwargs):
#         context = super(CarsPageView, self).get_context_data(**kwargs)
#         context['all_cars'] = Car.objects.all()
#         return context