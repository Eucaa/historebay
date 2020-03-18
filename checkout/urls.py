from django.conf.urls import url
from .views import checkout  # From the views.py file(in the checkout-folder), import the checkout-function.

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
]