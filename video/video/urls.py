"""video URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from app import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^$', views.index),
    url(r'^player_video/$', views.player_video),
    url(r'^project_video/$', views.project_video),
    url(r'^search/$', views.search),
    url(r'^login/$', views.login),
    url(r'^playercn_info/$', views.playercn_info),
    url(r'^player_list/$', views.player_list),
    url(r'^playercn_list/$', views.playercn_list),
    url(r'^match_list/$', views.match_list),
    url(r'^playercn_video/$', views.playercn_video),
    url(r'^upload/$', views.upload)

]
