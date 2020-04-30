from django.shortcuts import render
from django.contrib import messages
from products.models import Product
from categories.models import Category
from productType.models import ProductType


def search_filter(request):
    """
    Search filter to serach for products by matching the query
    made by whatever the user types into it.
    This build-in Django function works the same as SQL's
    SELECT...WHERE name ILIKE etc..
    """
    queryString = request.GET['q']
    categories = all_categories()
    productTypes = all_productTypes()

    if queryString is None or queryString == "":
        messages.error(request, 'No search input given.')
        return render(request, "products.html", {"categories": categories,
                                                 "productTypes": productTypes})

    products = Product.objects.filter(name__icontains=queryString)

    if len(products) == 0:
        messages.error(request, 'Item(s) not found. Please try again.')

    return render(request, "products.html", {"products": products,
                                             "categories": categories,
                                             "productTypes": productTypes})


def all_categories():
    return Category.objects.all()


def all_productTypes():
    return ProductType.objects.all()


def products_by_category(request, pk):
    """
    See products by category.
    """
    products = Product.objects.filter(category_id=pk)
    categories = all_categories()
    productTypes = all_productTypes()
    return render(request, "products.html", {"products": products,
                                             "categories": categories,
                                             "productTypes": productTypes})


def products_by_producttype(request, pk):
    """
    See products by product type.
    """
    products = Product.objects.filter(productType_id=pk)
    categories = all_categories()
    productTypes = all_productTypes()
    return render(request, "products.html", {"products": products,
                                             "categories": categories,
                                             "productTypes": productTypes})
