from django.db import models
from categories.models import Category
from productType.models import ProductType


# Create your models here.
class Product(models.Model):  # The Model is what will create the database for the product. 
    name = models.CharField(max_length=55, blank='')  # Empty default will not add a default product into the database.
    description = models.TextField(max_length=140)  # A box into which you can type text about the product.
    availability = models.IntegerField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # To add a price which is no larger that 6 digits and has a decimal placing after 2 digits.
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=None)
    productType = models.ForeignKey(ProductType, on_delete=None)

    def __str__(self):
        return self.name
