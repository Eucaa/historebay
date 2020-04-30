from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Product
from categories.models import Category
from productType.models import ProductType
import random
from django.http import JsonResponse
# import os
# from urllib.parse import unquote


def all_categories():
    return Category.objects.all()


def all_productTypes():
    return ProductType.objects.all()


def view_productDetails(request, pk):
    """
    View all details of the product.
    """
    productDetails = get_object_or_404(Product, pk=pk)
    categories = all_categories()
    productTypes = all_productTypes()
    categoryFromProduct = Category.objects.filter(id=productDetails.
                                                  category_id).first()
    productTypeFromProduct = ProductType.objects.filter(id=productDetails.
                                                        productType_id).first()
    cart = request.session.get('cart', {})
    quantity = 0
    try:
        quantity = cart[pk]
    except KeyError:
        print("Item not found in cart. Setting quantity to 0.")

    return render(request, "productDetails.html",
                  {"productDetails": productDetails, "categories": categories,
                   "productTypes": productTypes,
                   "categoryFromProduct": categoryFromProduct,
                   "productTypeFromProduct": productTypeFromProduct,
                   "quantity": quantity})


def adjust_cart_in_details(request, id):
    """
    Adjusts (increase/decrease) the quantity of the specified product
    to the specified amount.
    """
    quantity = request.POST.get('quantity')
    quantityAdjust = request.POST.get('quantity')
    if quantityAdjust == "":
        messages.error(request, 'Adjust quantity')
        return redirect(reverse('productDetails', kwargs={'pk': id}))

    try:
        int(quantityAdjust)
    except ValueError:
        messages.error(request, 'Adjust quantity')
        return redirect(reverse('productDetails', kwargs={'pk': id}))

    quantity = int(quantityAdjust)

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def listing(request):
    """
    Functionality of the pagination
    to show 3 items per page.
    """
    product_list = list(Product.objects.all())
    page = request.GET.get('page')
    categories = Category.objects.all()
    productTypes = ProductType.objects.all()
    if page is None:
        random.shuffle(product_list)

    paginator = Paginator(product_list, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:

        products = paginator.page(1)
    except EmptyPage:

        products = paginator.page(paginator.num_pages)
    print(products)
    return render(request, "products.html", {"products": products,
                                             "categories": categories,
                                             "productTypes": productTypes})


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


def search_products(request):
    """
    Find items based on the query input.
    """
    query = request.GET.get('query')
    product_list = list(Product.objects.filter(name__icontains=query).values())
    return JsonResponse(product_list, safe=False)
