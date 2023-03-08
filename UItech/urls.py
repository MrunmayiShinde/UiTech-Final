"""UItech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from log import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('temp/',views.temp,name='temp'),
    path('B1/',views.B1,name='B1'),
    path('B1A/',views.B1A,name='B1A'),
    path('B1B/',views.B1B,name='B1B'),
    path('B2/',views.B2,name='B2'),
    path('B3/',views.B3,name='B3'),
    path('B4/',views.B4,name='B4'),
    path('B5/',views.B5,name='B5'),
    path('B6/',views.B6,name='B6'),
    path('logout/',views.logout,name='logout'),
    path('cert/',views.cert,name='cert')
]

