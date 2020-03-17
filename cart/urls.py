from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart


urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
]

# Include the above urls as cart.urls.py in the top-level urls (ehcommerce-folder), for activation.
# Explanation of cart.urls.py: cart(folder).urls.py(file).
