from django.db import models
from categories.models import Category
from productType.models import ProductType
import base64
import uuid


class Product(models.Model):
    name = models.CharField(max_length=55, blank='')
    description = models.TextField(max_length=140)
    availability = models.IntegerField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
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
