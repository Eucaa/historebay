from django import forms
from .models import Order


# Create a make-payment form.
class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]  # Gives a list of choices for the exparation month of the debit/ credit card.
    YEAR_CHOICES = [(i, i) for i in range(2019, 2040)]  # Gives a list of choices for the exparation year of the debit/ credit card. This one will have to get updated eventually.

    credit_card_number = forms.CharField(label='Credit card number', required=False)  # Field to fill in the credit cards number. Required field, cannot be left blank.
    cvv = forms.CharField(label='Security code (CVV)', required=False)  # Three digit number field, which is used for online payments. Required field (for Stripe), cannot be left blank.
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)  # ChoiceField is like a dropdown with selected choices, in this case months. Used from MONTH_CHOICES =
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)  # ChoiceField is like a dropdown with selected choices, in this case months. Used from YEAR_CHOICES =
    # Encryption of the credit card is done by Stripe and it's JS codes. Therefore, "required=False"  can be used.
    stripe_id = forms.CharField(widget=forms.HiddenInput)  # Stripe requires the ID, but although it's inputted in the form here, the costumer will NOT see it.


# Create an order-form.
class OrderForm(forms.ModelForm):  #  The form just contains a series of fields to enter the information that is in that database in that model. Like full_name, postcode, county etc.
    last_name = forms.CharField(label='last name', required=False)
    class Meta:
        model = Order  # Uses the Order-class created in models.py
        fields = (
            'last_name', 'first_name', 'street_address1', 'street_address2',
            'postcode', 'town_or_city', 'country', 'phone_number'
            )
