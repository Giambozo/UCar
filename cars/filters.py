import django_filters

from cars.models import Car


class CarFilter(django_filters.FilterSet):
    car_title = django_filters.CharFilter(lookup_expr='iexact')
    model = django_filters.CharFilter(lookup_expr='iexact')
    year = django_filters.CharFilter(lookup_expr='iexact')
    state = django_filters.CharFilter(lookup_expr='iexact')
    price = django_filters.CharFilter(lookup_expr='iexact')
    body_style = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Car
        fields = ['car_title', 'model', 'year', 'state', 'price', "body_style"]
