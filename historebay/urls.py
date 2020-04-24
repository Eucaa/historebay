"""historebay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from products import urls as urls_products  # From the products-folder, in the urls.py file, import the urls as urls_products.
#from products.views import all_products  # From the views.py file in the products-folder, import the all_products function.
from cart import urls as urls_cart  # From the cart folder, import the urls as urls_cart.
from search import urls as urls_search
from checkout import urls as urls_checkout
from django.views import static  # Import the static folder (and substance).
from .settings import MEDIA_ROOT, BASE_DIR  # From the settings.py file, import the MEDIA_ROOT.
from products.views import listing
from contact_info import urls as urls_contact_info
import os


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', listing, name='index'),  # If there's no name after the slash/ in the URL, then just display all_products of the very first page.
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),  # Include all our URLs from the products app(folder).
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),  # Because of the use of images in media, add this specific (Django-standard) media URL.
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': os.path.join(BASE_DIR, "static")}), 
    url(r'^contact_info/', include(urls_contact_info)),
]
