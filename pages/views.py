from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

class HomePageView(TemplateView):
    template_name = 'pages/home.html'