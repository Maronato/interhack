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
from django.conf.urls import url, TemplateView
from django.contrib import admin
import main.views
import registration.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^update/$', registration.views.mailchimp_update, name='update'),
    url(r'^$', main.views.index, name='index'),
    url(r'^registration/$', registration.views.pre_registration, name='pre-reg'),
    url(r'^\.well-known/acme-challenge/0iTD0Vg-XGlO1M-MeBvaMgbuut8PjwenjP4DgV2xrlA', TemplateView.as_view(template_name="ssl.html")),
]
