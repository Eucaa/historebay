from django.conf.urls import url, include
from .views import listing, view_productDetails, adjust_cart_in_details, products_by_category, products_by_producttype, search_products

urlpatterns = [
    url(r'^$', listing, name='products'),
    url(r'^search_products$', search_products, name='search_products'),
    url(r'^view/(?P<pk>\d+)/$', view_productDetails, name='productDetails'),
    url(r'^adjust/(?P<id>\d+)/$', adjust_cart_in_details,
        name='adjust_cart_in_details'),
    url(r'^categoryview/(?P<pk>\d+)/$', products_by_category,
        name='products_by_category'),
    url(r'^productType/(?P<pk>\d+)/$', products_by_producttype,
        name='products_by_producttype'),
]
