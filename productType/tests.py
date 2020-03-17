from django.test import TestCase
from .models import ProductType
# Create your tests here.


class ProductTypeTests(TestCase):

    def test_str(self):
        test_name = ProductType(name='belp')
        self.assertEqual(str(test_name), 'blep')
