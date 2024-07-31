from django.shortcuts import render, redirect
from .forms import CategoryForm, EmployeeForm, ItemForm, OrderForm, SupplierForm, TestForm, UnitForm 
from .models import *
from django.core.paginator import Paginator
from .filters import *

# Create your views here.
def unitview(request):
    units = Unit.objects.all()
    context_Unt = {'uts':units}
    return render(request, 'Unit.html', context_Unt)

def test(request):
    if request.method =='POST':
        form = TestForm(request.POST)
    else:    
        form = TestForm()
    context = {'form':form}
    return render(request, 'test.html', context)

def category_view(request):
    page_number = request.GET.get('page')
    filter = CategoryFilter(request.GET, queryset=Category.objects.all())
    categories = filter.qs
    paginator = Paginator(categories, 3)
    page = paginator.page(page_number)
    
    if request.method =='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            #save
    else:    
        form = CategoryForm()
    context = {'form':form, 'page':page}
    return render(request, 'Category.html', context)

def unit_view(request):
    page_number = request.GET.get('page')
    filter = UnitFilter(request.GET, queryset=Unit.objects.all())
    units = filter.qs
    paginator = Paginator(units, 3)
    page = paginator.page(page_number)
    
    if request.method =='POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
        
    else:    
        form = UnitForm()
    context = {'form':form, 'filter':filter}
    return render(request, 'Unit.html', context)

def item_view(request):
    page_number = request.GET.get('page')
    filter = ItemFilter(request.GET, queryset=Item.objects.all())
    items = filter.qs
    paginator = Paginator(items, 3)
    page = paginator.page(page_number)
    page = paginator.page(1, 2, 3)
    if request.method =='POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        #save
    else:    
        form = ItemForm()
    
    return render(request, 'item.html', {'form':form, 'page':page})

def supplier_view(request):
    suppliers = Supplier.objects.all()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_view')
    else:    
        form = SupplierForm()
    return render(request, 'supplier.html', {'form': form, 'suppliers': suppliers})

def order_view(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form, 'orders': orders})


def employee_view(request):
    employees = Employee.objects.all() 
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            #save
    else:    
        form = EmployeeForm()
    context = {'form':form, 'employs':employees}
    return render(request, 'employee.html', context)


