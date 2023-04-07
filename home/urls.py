"""adpublicize URL Configuration

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
from home import views
from .views import download_receipt

urlpatterns = [
    path("", views.index, name="home"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("signup", views.signup, name="signup"),
    path("profile", views.profile, name="profile"),
    path("history", views.history, name="history"),
    path("slot", views.slot, name="slot"),
    path("slot_details", views.slot_details, name="slot_details"),
    path("receipt", views.receipt, name="receipt"),
    path('download-receipt/', download_receipt, name='download-receipt'),
    path('login/', views.login_view, name='login'),
    # path('delete-users/', views.delete_users, name='delete_users'),
]
