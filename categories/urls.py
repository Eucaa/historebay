from django.conf.urls import url
from .views import show_category


urlpatterns = [
    url(r'^category/(?P<categoryList>.+)/$', show_category, name='category'),
]
