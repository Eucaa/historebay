from django.conf.urls import url, include
from .views import logout, login, registration, user_profile
from accounts import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name='logout'),  # Refers to "{% url 'logout' %}" in the base.html template.
    url(r'^login/$', login, name='login'),  # Refers to "{% url 'login' %}" in the base.html template.
    url(r'^registration/$', registration, name='registration'),  # Refers to "{% url 'registration' %}" in the base.html template.
    url(r'^profile/$', user_profile, name='profile'),   # Refers to "{% url 'profile' %}" in the base.html template.
    url(r'^password-reset/', include(url_reset))  # With this, all of the urlpatterns in the url_reset.py file, will be connected to this url.
]
