from django.db import models
from products.models import Product  # Import the product model so that the ordered items are shown and ready to be bought.

# Create your models here.


# To acquire information from the costumer who want to buy products.
class Order(models.Model):
    last_name = models.CharField(max_length=50, blank=False)  # Can be up to max 50 characters and must be filled in.
    first_name = models.CharField(max_length=50, blank=False)
    street_address1 = models.CharField(max_length=50, blank=False)
    street_address2 = models.CharField(max_length=50, blank=True)  # second address line can be blank. 
    postcode = models.CharField(max_length=20, blank=True)  # Postal code CAN be blank, cause not everyone has one.
    town_or_city = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    date = models.DateField()  # Shows an automated date field to add whatever you like.

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.id, self.date, self.first_name, self.last_name)  # This will inject and return the information into the appointed stings.


# This is to check which product is being purcahsed.
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)  # Data from the costumer.
    product = models.ForeignKey(Product, null=False)  # Data from the Product, as imported above.
    quantity = models.IntegerField(blank=False)  # Data of how many items the costumer is going to buy.

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price)  # This will inject and return the information into the appointed stings.
