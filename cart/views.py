from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.


def view_cart(request):
    """ A view(page) that renders the cart content. """
    return render(request, "cart.html")  # No need to pass in a dictionary of cart_contents because that context is available everywhere.


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

    quantity = int(quantityVal)  # Gets an integer from the form(context.py-file). It gives the option to increase and decrease the number of items.

    cart = request.session.get('cart', {})  # The cart requests the existing cart (session) if there is one, or a blank dictionary if there is nothing. This is placed it the context.py file
    if id in cart:  # If-statement for adding two items with same id, without overwriting the value.
        cart[id] = int(cart[id]) + quantity  # This will add a new quantity to the excisting quantity.
    else:
        cart[id] = cart.get(id, quantity)       # ... and what we add is an ID and a quantity.

    request.session['cart'] = cart
    return redirect(reverse("index"))


def adjust_cart(request, id):
    """ Adjusts (increase/decrease) the quantity of the specified product to the specified amount """
    quantity = request.POST.get('quantity')  # Gets the existing quantity as an integer. Adjust what's currently in the cart in the current session, when needed.

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

    # Only adjust when the quantity is greater than '0':
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)   # If there's nothing in the cart, there is nothing to adjust. So it takes out the id (.pop()) and returns back to the view_cart url-area.

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
