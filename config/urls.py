from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("class_management.urls")),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('accounts/', include('django.contrib.auth.urls')),
]
