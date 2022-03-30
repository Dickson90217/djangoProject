"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.urls import path
from mywork import views

urlpatterns = [
    path('howard/', views.hello, name='home'),
    path('login/', views.login),
    path('kind',  views.kind),
    path('animals',  views.animals),
    path('catts',  views.catts),
    path('others',  views.others),
    path('dogproject',views.dogproject)
    ]