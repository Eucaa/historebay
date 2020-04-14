from django.shortcuts import render
from categories.models import Category
from productType.models import ProductType


def all_categories():
    return Category.objects.all()


def all_productTypes():
    return ProductType.objects.all()


def about(request):
    categories = all_categories()
    productTypes = all_productTypes()
    return render(request, 'about.html', {"categories": categories, "productTypes": productTypes})


def tac(request):
    categories = all_categories()
    productTypes = all_productTypes()
    return render(request, 'tac.html', {"categories": categories, "productTypes": productTypes})


def pac(request):
    categories = all_categories()
    productTypes = all_productTypes()
    return render(request, 'pac.html', {"categories": categories, "productTypes": productTypes})


def contact(request):
    categories = all_categories()
    productTypes = all_productTypes()
    return render(request, 'contact.html', {"categories": categories, "productTypes": productTypes})
