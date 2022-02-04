from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
#import mywebsite.apps.public.urls as url_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('mywebsite.apps.public.urls')),
    path("accounts/", include('mywebsite.apps.accounts.urls')),

]
