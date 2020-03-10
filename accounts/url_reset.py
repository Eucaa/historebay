from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^$', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    url(r'^done/$', password_reset_done, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,  # This url wil create a new (temp) password for every (password) reset....
        {'post_reset_confirm': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),  # ...and will redirect them to an url to achieve this.
    url(r'^complete/$', password_reset_complete, name='password_reset_complete')
]
