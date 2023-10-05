from django_filters import rest_framework as filters
from core.models import *


class CardOperationFilter(filters.FilterSet):
    date = filters.DateFilter(field_name='date', lookup_expr='exact', label='Дата (гггг-мм-дд)')
    station = filters.ModelChoiceFilter(
        field_name='station',
        queryset=Station.objects.all(),
        label='АЗС',
        empty_label='Выберите АЗС'
    )
    card = filters.ModelChoiceFilter(
        field_name='card',
        queryset=Station.objects.all(),
        label='Карта',
        empty_label='Выберите карту'
    )
    fuel_type = filters.ModelChoiceFilter(
        field_name='fuel_type',
        queryset=Station.objects.all(),
        label='Тип топлива',
        empty_label='Выберите тип топлива'
    )
    operation_type = filters.ModelChoiceFilter(
        field_name='operation_type',
        queryset=Station.objects.all(),
        label='Тип операции',
        empty_label='Выберите тип операции'
    )

    class Meta:
        model = CardOperation
        fields = ['date', 'station', 'card', 'fuel_type', 'operation_type']

