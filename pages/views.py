from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from cars.models import Car
from pages.models import Team

from .models import Team


# Create your views here.

class HomePageView(ListView):
    model = Team
    template_name = 'pages/home.html'

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
