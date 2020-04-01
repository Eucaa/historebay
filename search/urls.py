from django.conf.urls import url
from .views import search_filter  # From the views folder in the search file, import the `do_search` funcion.
from products.views import products_by_category, products_by_producttype

# Add the url's below to the urls.py file in the ehcommerce folder.
urlpatterns = [
    url(r'^$', search_filter, name='search'),
    url(r'^categoryview/(?P<pk>\d+)/$', products_by_category, name='products_by_category'),
    url(r'^productType/(?P<pk>\d+)/$', products_by_producttype, name='products_by_producttype'),
]
