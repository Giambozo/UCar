"""
URL configuration for UCar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cars import views

urlpatterns = [
    # path('', views.CarsPageView.as_view(), name="cars"),
    path('', views.cars, name='cars'),
    path('<int:pk>', views.CarSinglePageView.as_view(), name="car_detail"),
    path('search', views.search, name="search"),
    #path('search', views.SearchView.as_view(), name="search")
]
