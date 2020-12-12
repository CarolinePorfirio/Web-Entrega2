"""welcomechile URL Configuration

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
from django.urls import path
from django.urls import include

from core import views as core_views
from contact import views as contact_views 
from turismo import views as turismo_views
from registration import views as registration_views

from django.conf import settings

urlpatterns = [
    path('',core_views.home, name='home'),
    path('index',core_views.home, name='home'),
    path('quiensomos',core_views.quiensomos, name='quiensomos'),
    path('tramites',core_views.tramites, name='tramites'),
    path('turismo',turismo_views.turismo, name='turismo'),
    path('preguntas',core_views.preguntas, name='preguntas'),
    path('contacto',contact_views.contacto, name='contacto'),
    path('backoffice',registration_views.backoffice, name='backoffice'),
    path('admin/', admin.site.urls),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

