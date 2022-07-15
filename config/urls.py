"""maid URL Configuration

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
from django.contrib import admin
from django.urls import path
from app.accounts.views import AccountsView, AccountsRegisterView, AccountsComplementRegisterView, HomeView, AccountsEmpolyerProfilesView

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('entrar', AccountsView.as_view(), name='accounts'),
    path('cadastro', AccountsRegisterView.as_view(), name='register'),
    path('complemento', AccountsComplementRegisterView.as_view(), name='complement_register'),
    path('perfil', AccountsEmpolyerProfilesView.as_view(), name='employer_profile'),
    path('dash/', admin.site.urls)

]

admin.site.site_header = 'Maid Match'
admin.site.site_title = 'Maid Match'
admin.site.index_title = 'Maid Match'
