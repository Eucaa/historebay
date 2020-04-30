from django.conf.urls import url
from .views import search_filter
from products.views import products_by_category, products_by_producttype


urlpatterns = [
    url(r'^$', search_filter, name='search'),
    url(r'^categoryview/(?P<pk>\d+)/$', products_by_category,
        name='products_by_category'),
    url(r'^productType/(?P<pk>\d+)/$', products_by_producttype,
        name='products_by_producttype'),
]
