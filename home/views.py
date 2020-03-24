from django.shortcuts import render
from categories.models import Category
from productType.models import ProductType


def all_categories():
    return Category.objects.all()


def all_productTypes():
    return ProductType.objects.all()


# Create your views here.
def index(request):
    """A view that displays the index page"""
    categories = all_categories()
    productTypes = all_productTypes()
    return render(request, "index.html", {"categories": categories, "productTypes": productTypes})
