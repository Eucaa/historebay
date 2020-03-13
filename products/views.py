from django.shortcuts import render
from .models import Product
# Create your views here.


def all_products(request):
    products = Product.object.all()  # returns all products in the database.
    return render(request, "products.html", {"products": products})  # Render a products.html page. And within that page, we will have access to all products.
