"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from qa import views

urlpatterns = [
    url(r'^login/$', views.logining),
    url(r'^question/(?P<questionId>\d+)/$', views.single),
    url(r'^ask/.*$',views.ask),
    url(r'^popular/$', views.most_related),
    url(r'^new/$',views.test),
    url(r'^\?page\=\d+$',views.latest),
    url(r'^answer/$', views.answer),
    url(r'^$',views.latest),
    url(r'^signup/$', views.signup),
]
