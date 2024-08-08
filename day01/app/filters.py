import django_filters
from .models import Category, Item, Unit

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = '__all__'
        
class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['name', 'category', 'unit']
        
