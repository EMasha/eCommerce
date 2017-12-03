from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
# Create your views here.
def home(request):
    category = Category.objects.all()
    products=Product.objects.filter(available=True)
    return render(request, 'MyShop/index.html', {'category':category, 'products':products})

def products(request, category_slug=None):
    category = None
    categories = Category.objects.filter()
    prodcts = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        prodcts = prodcts.filter(category=category)
    return render(request, 'MyShop/products.html', {'category': category, 'categories': categories, 'products':prodcts})
