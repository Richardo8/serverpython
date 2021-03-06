"""server URL Configuration

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
from learn import views as learn_views
from calc import views as calc_views
from userlist import views as userlist_views
from article import views as article_views

urlpatterns = [
    url(r'^$', calc_views.index, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^add/$', calc_views.add, name='add'),
    url(r'^addOptimize/(\d+)/(\d+)/$', calc_views.addOptimize, name='addOptimize'),
    url(r'^userlist', userlist_views.getAllUser, name='readfile'),
    url(r'^search', userlist_views.search, name='search'),
    url(r'^upload', article_views.uploadPic, name='upload')
]
