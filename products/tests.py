from django.test import TestCase
from .models import Product
# Create your tests here.


class ProductTests(TestCase):

    def test_str(self):
        test_name = Product(name='An item')
        self.assertEqual(str(test_name), 'An item')
