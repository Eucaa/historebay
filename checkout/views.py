from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OrderForm, MakePaymentForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
from categories.models import Category
from productType.models import ProductType
import stripe

"""
Requires the API's of Stripe, which are set in the settings.py file.
"""
stripe.api_key = settings.STRIPE_SECRET


def all_categories():
    return Category.objects.all()


def all_productTypes():
    return ProductType.objects.all()


def check_input_fields(request, order_form):
    """
    Creates the form to fill in the data for the payment
    """
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
    """
    This method will check the validity of the filled in data and the data of
    what is in the cart.
    A payment will commence once the cart details have been calculated.
    """
    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if check_input_fields(request, order_form) is False:
            payment_form = MakePaymentForm()
            return render(request, "checkout.html",
                          {"order_form": order_form,
                           "payment_form": payment_form,
                           "publishable": settings.STRIPE_PUBLISHABLE})

        payment_form = MakePaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                product.availability = product.availability - quantity
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity,
                )
                order_line_item.save()
                product.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )

            except stripe.error.CardError:
                messages.error(request, "Your card was declined")

            if customer.paid:
                messages.error(request, "Payment successful")
                request.session['cart'] = {}
                print('puchase complete')
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "Unable to take a payment with this card")

    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    categories = all_categories()
    productTypes = all_productTypes()
    return render(request, "checkout.html",
                  {"categories": categories, "productTypes": productTypes,
                   "order_form": order_form, "payment_form": payment_form,
                   "publishable": settings.STRIPE_PUBLISHABLE})
