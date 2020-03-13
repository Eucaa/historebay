from django.conf.urls import url, include # This import will link to the top-level URL's in the historebay-directory (so the eg. the historebay- as well as the accounts-folder).
from .views import all_products


urlpatterns = [
    url(r'^$', all_products, name='products'),
]

# This will show the all_products view(function). Add this url to to the list in the main urls.py file (historebay/urls.py)
