from django.db import models


# Create your models here.
class Item(models.Model):  # The Model is what will create the database for the item. 
    name = models.CharField(max_length=55, blank='')  # Empty default will not add a default porduct into the database.
    description = models.TextField()  # A box into which you can type text about the item.
    price = models.DecimalField(max_digits=6, decimal_places=2)  # To add a price which is no larger that 6 digits and has a decimal placing after 2 digits.
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
