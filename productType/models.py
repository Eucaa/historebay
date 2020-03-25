from django.db import models


# Create your models here.
class ProductType(models.Model):  # The Model is what will create the database for the product. 
    name = models.CharField(max_length=25, blank='')  # Empty default will not add a default product into the database.

    def __str__(self):
        return self.name
