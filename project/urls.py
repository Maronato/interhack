"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
import main.views
import registration.views
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^update/$', registration.views.mailchimp_update, name='update'),
    url(r'^(referral/(?P<referee_id>\w+)/)?$', main.views.index, name='index'),
    url(r'^registration/$', registration.views.pre_registration, name='pre-reg'),
    url(r'^\.well-known/acme-challenge/KzB9zOzwjww1N_W7re_bNqct4m3tTRByFIAXX3YdnF8', TemplateView.as_view(template_name="main/ssl.html")),
    url(r'^MoreInfo/$', RedirectView.as_view(url="http://agency.bemyapp.com/insights/infographics-hackathon-figures-in-2016.html")),
]
