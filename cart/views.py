from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from categories.models import Category
from productType.models import ProductType


def all_categories():
    return Category.objects.all()


def all_productTypes():
    return ProductType.objects.all()


def view_cart(request):
    """ A view(page) that renders the cart content. """
    categories = all_categories()
    productTypes = all_productTypes()
    return render(request, "cart.html", {"categories": categories,
                                         "productTypes": productTypes})


def add_to_cart(request, id):
    """ Add a quantity of the specified product to the cart """
    quantityVal = request.POST.get('quantity')
    if quantityVal == "":
        messages.error(request, 'Add a quantity')
        return redirect(reverse('index'))

    try:
        int(quantityVal)
    except ValueError:
        messages.error(request, 'Add a quantity')
        return redirect(reverse('index'))

    quantity = int(quantityVal)

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse("index"))


def adjust_cart(request, id):
    """ Adjusts (increase/decrease) the quantity of the specified product
        to the specified amount """
    quantity = request.POST.get('quantity')

    quantityAdjust = request.POST.get('quantity')
    if quantityAdjust == "":
        messages.error(request, 'Adjust quantity')
        return redirect(reverse('view_cart'))

    try:
        int(quantityAdjust)
    except ValueError:
        messages.error(request, 'Adjust quantity')
        return redirect(reverse('view_cart'))

    quantity = int(quantityAdjust)

    cart = request.session.get('cart', {})

    """Only adjust when the quantity is greater than '0'"""
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_from_cart(request, id):
    """Delete item from cart by resetting to zero"""
    request.POST = request.POST.copy()
    request.POST['quantity'] = 0
    return adjust_cart(request, id)
