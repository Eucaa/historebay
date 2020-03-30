from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required  # Because customers needs to be logged in when they purchase something, import `auth.decorators`.
from django.contrib import messages  # To be able to show the error message as written on line 49.
from .forms import OrderForm, MakePaymentForm  # These are imported from the forms.py file.
from .models import OrderLineItem
from django.conf import settings  # Import settings.py to get the Stripe key/value settings from the settings.py file.
from django.utils import timezone
from products.models import Product  # From the products app(folder), import the class Product to activate line 29 below here.
from categories.models import Category
from productType.models import ProductType
import stripe

# Create your views here.
# Requires the API's of Stripe, which are set in the settings.py file.
stripe.api_key = settings.STRIPE_SECRET


def all_categories():
    return Category.objects.all()


def all_productTypes():
    return ProductType.objects.all()


def check_input_fields(request, order_form):
    lastName = order_form['last_name'].value()
    firstName = order_form['first_name'].value()
    streetAddress1 = order_form['street_address1'].value()
    townOrCity = order_form['town_or_city'].value()
    country = order_form['country'].value()
    phoneNumber = order_form['phone_number'].value()

    if lastName is None or lastName == "":
        messages.error(request, 'last name is required')
        return False
    if firstName is None or firstName == "":
        messages.error(request, 'first name is required')
        return False
    if streetAddress1 is None or streetAddress1 == "":
        messages.error(request, 'street name required')
        return False
    if townOrCity is None or townOrCity == "":
        messages.error(request, 'name town or city is required')
        return False
    if country is None or country == "":
        messages.error(request, 'name or country required')
        return False
    if phoneNumber is None or phoneNumber == "":
        messages.error(request, 'phone number is required')
        return False

    return True


@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)  # The order form is what contains their name, address, and so on.

        # Check if all my inputs are valid.
        if check_input_fields(request, order_form) is False:
            payment_form = MakePaymentForm()
            return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})

        payment_form = MakePaymentForm(request.POST)  # The payment form is what contains the credit card or debit card details.
        # when the order_form and payment_form are both valid(filled in correctly), then the order_form will be saved as an order.
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()  # Notes the time when the button was clicked to confirm the order.
            order.save()  # actually save the order

            # Get the data from the cart, from the current session, to check which items are being purchased.
            cart = request.session.get('cart', {})  # Start at 0 and loop over the ID and the quantity of the cart.items to get the products.
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                product.availability = product.availability - quantity
                total += quantity * product.price  # Get the total, add a quantity and multiply by the product price. This will give the total price.
                order_line_item = OrderLineItem(  # Get the above created objects and combine them with the OrderLineItem class in the models.py file...
                    order=order,
                    product=product,
                    quantity=quantity,
                )
                order_line_item.save()  # ... and save them. This will show the details of what's being purchased.
                product.save()

            # Using the build-in API from Stripe, try to create a customer charge...
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),  # Stripe charges everything in cents, so it the total amount of cents x 100...
                    currency="EUR",
                    description=request.user.email,  # When going to the Stripe dashboard, you'll be able to see who the payment came from.
                    card=payment_form.cleaned_data['stripe_id'],
                )
            # ... when the payment (with use of Stripe) does not go through, then throw in an error.
            except stripe.error.CardError:
                messages.error(request, "Your card was declined")

            # If the payment was successful or not, then throw in another message.
            if customer.paid:
                messages.error(request, "Payment successful")
                request.session['cart'] = {}
                return redirect(reverse('products'))  # This will redirect the user back to the products.html page.
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "Unable to take a payment with this card")  # This else: is to cover the `if order_form.is_valid() and payment_form.is_valid():' -loop on line 22. 

    else:  # Return a blank form (cover for if-loop on line 17)
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    categories = all_categories()
    productTypes = all_productTypes()
    # Return a view called 'checkout.html' and include the order_form and the payment_form in there.
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE, "categories": categories, "productTypes": productTypes})
