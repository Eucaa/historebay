from django.shortcuts import render
from products.models import Product
from categories.models import Category
from productType.models import ProductType
# Create your models here.


def search_filter(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])  # filter() is a built-in function from Django. name__icontains works like the SQL: SELECT...WHERE name ILIKE etc..
                                                                         # The form to filter for items is called 'q' (this time). 
                                                                         # Whatever you type into it will be used to filter for matching products.
    categories = all_categories()
    productTypes = all_productTypes()
    return render(request, "products.html", {'products': products, "categories": categories, "productTypes": productTypes})


def all_categories():
    return Category.objects.all()


def all_productTypes():
    return ProductType.objects.all()


def products_by_category(request, pk):
    products = Product.objects.filter(category_id=pk)
    categories = all_categories()
    productTypes = all_productTypes()
    return render(request, "products.html", {"products": products, "categories": categories, "productTypes": productTypes})


def products_by_producttype(request, pk):
    products = Product.objects.filter(productType_id=pk)
    categories = all_categories()
    productTypes = all_productTypes()
    return render(request, "products.html", {"products": products, "categories": categories, "productTypes": productTypes})