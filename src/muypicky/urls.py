from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^u/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    url(r'^items/', include(('menus.urls', 'menus'), namespace='menus')),
    url(r'^restaurants/', include(('restaurants.urls', 'restaurants'), namespace='restaurants')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
]