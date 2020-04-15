from django.shortcuts import get_object_or_404
from products.models import Product


#  This time, a class function will not be created (as eg. in the prodicts-app(folder) under models.py, since the selected items will not have to be saved once the user closes the browser.)
def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every web page of the application.
    """
    cart = request.session.get('cart', {})  # The cart requests the existing cart (session) if there is one, or a blank dictionary if there is nothing. This is placed it the views.py file.

    # Initialize the data from the cart so the user can see what's in there.
    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():  # The ID will be which product ID it is, and the quantity is how many the user wishes to purchase. The item() in this line is a Python method.
        product = get_object_or_404(Product, pk=id)  # Get the products from the products-folder/models.py file, use the primary key as the unique id(cause every product gets and unique id).
        total += quantity * product.price  # Take the quantity of items multiplied by their price and add them to a continuous running total of the cost.
        product_count += quantity  # As you add more quantity as a user, the product count goes up.
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})  # Join the cart items to the cart by id, so there'll always what product has been added and how many.
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}  # Return the key-value pairs in a dict-shape.
    """
    Add 'cart.contexts.cart_contents',  to the 'context_processors': [..
    under TEMPLATES in the settings.py file.
    """


