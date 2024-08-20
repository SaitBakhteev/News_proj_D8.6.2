from django.forms import DateInput
from django_filters import FilterSet, CharFilter, DateFilter



class PostFilter(FilterSet): # класс фильтра для поиска новостей
    search_title = CharFilter(lookup_expr='iregex', label='Название', field_name= 'title') # название статьи/новости
    search_author = CharFilter(lookup_expr='iregex', label='Автор', field_name= 'author__user__username') # название статьи/новости
    search_date = DateFilter(field_name='create_time', lookup_expr='gte', # это поле фильтра для поиска статей, позже указанной даты
                 label='Дата, начиная с которой вышли посты', widget=DateInput(attrs={'type': 'date'}, format='%d%m%Y'))




