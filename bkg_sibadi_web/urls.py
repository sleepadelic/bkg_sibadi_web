"""bkg_sibadi_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
import bkg.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bkg.views.index, name='index'),
    path('issues_list/', bkg.views.issues_list, name='issues_list'),
    path('issues_listp/<int:page_num>', bkg.views.issues_list_page, name='issues_list_page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
