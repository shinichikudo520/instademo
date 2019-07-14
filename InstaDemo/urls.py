"""InstaDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from Insta.views import SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Insta.urls')),
    # django.contrib.auth是django自带的一个app，跟Insta一样，它也有自己的urls，指定了路径http://127.0.0.1:8000/auth/login/跳转到/registration/login.html
    path('auth/',include('django.contrib.auth.urls')),# 必须在template下创建一个叫registration的文件夹，文件夹下找一个login.html
    # 在setting.py中设置post成功的重定向路径 LOGIN_REDIRECT_URL = 'home'
    path('auth/signup/',SignupView.as_view(),name='signup'),# 必须在template下创建一个叫registration的文件夹，文件夹下找一个login.html


]

# Content Management System