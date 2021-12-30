from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", mainapp.main),
    path("product/", mainapp.products),
    path("contact/", mainapp.contact),
]
