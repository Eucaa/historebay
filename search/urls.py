from django.conf.urls import url
from .views import search_filter  # From the views folder in the search file, import the `do_search` funcion.

# Add the url's below to the urls.py file in the ehcommerce folder.
urlpatterns = [
    url(r'^$', search_filter, name='search'),
]
