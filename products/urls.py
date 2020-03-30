from django.conf.urls import url, include  # This import will link to the top-level URL's in the historebay-directory (so the eg. the historebay- as well as the accounts-folder).
from .views import listing, view_productDetails, adjust_cart_in_details

urlpatterns = [
    url(r'^$', listing, name='products'),
    url(r'^view/(?P<pk>\d+)/$', view_productDetails, name='productDetails'),
    url(r'^adjust/(?P<id>\d+)/$', adjust_cart_in_details, name='adjust_cart_in_details'),
]

# This will show the all_products view(function). Add this url to to the list in the main urls.py file (historebay/urls.py)
