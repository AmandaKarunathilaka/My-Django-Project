from django.contrib import admin
from .models import Category, Employee, Item,Unit,Supplier, Order

# Register your models here.
admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Item)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(Employee)