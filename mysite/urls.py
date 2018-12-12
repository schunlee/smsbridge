from django.conf.urls import include, url
from django.contrib import admin

from .view import redirect_view

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sms/', include('sms.urls')),
    url(r'^$', redirect_view),
]
