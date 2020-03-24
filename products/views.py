from django.shortcuts import render
from .models import Product
from categories.models import Category
from productType.models import ProductType
# Create your views here.


def all_categories():
    return Category.objects.all()


def all_productTypes():
    return ProductType.objects.all()


def all_products(request):
    products = Product.objects.all()  # returns all products in the database.
    categories = all_categories()
    productTypes = all_productTypes()
    return render(request, "products.html", {"products": products, "categories": categories, "productTypes": productTypes})  # Render a products.html page. And within that page, we will have access to all products.
