from django.conf.urls import url
from .views import about, tac, pac, contact

urlpatterns = [
    url(r'^about$', about, name='about'),
    url(r'^tac$', tac, name='tac'),
    url(r'^pac$', pac, name='pac'),
    url(r'^contact$', contact, name='contact'),
]
