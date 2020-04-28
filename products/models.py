from django.db import models
from categories.models import Category
from productType.models import ProductType
import base64
import uuid

# Create your models here.
class Product(models.Model):  # The Model is what will create the database for the product. 
    name = models.CharField(max_length=55, blank='')  # Empty default will not add a default product into the database.
    description = models.TextField(max_length=140)  # A box into which you can type text about the product.
    availability = models.IntegerField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # To add a price which is no larger that 6 digits and has a decimal placing after 2 digits.
    image = models.FileField(upload_to='images')
    image_as_base64 = models.TextField(blank=True, editable=False)
    category = models.ForeignKey(Category, on_delete=None)
    productType = models.ForeignKey(ProductType, on_delete=None)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.image_as_base64 == "":
            self.image_as_base64 = base64.b64encode(self.image.file.read())

            newFilename = str(uuid.uuid4())
            with open(newFilename, 'wb') as f:
                f.write(base64.b64decode(self.image_as_base64))
            self.image = newFilename
        super(Product, self).save(*args, **kwargs)

    def get_image_data(self):
        return 'data:image;base64,%s' % (self.image_as_base64)
