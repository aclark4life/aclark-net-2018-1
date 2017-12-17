"""aclarknet URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from aclarknet.www import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^admin', admin.site.urls),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^book$', views.book, name='book'),
    url(r'^clients$', views.clients, name='clients'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^community$', views.community, name='community'),
    url(r'^open-source$', views.opensource, name='open-source'),
    url(r'^projects$', views.projects, name='projects'),
    url(r'^services$', views.services, name='services'),
    url(r'^team$', views.team, name='team'),
    url(r'^testimonials$', views.testimonials, name='testimonials'),
    url(r'^location$', views.location, name='location'),
    url(r'^history$', views.history, name='history'),
    url(r'^now$', views.now, name='now'),
]
