"""
URL configuration for apm_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("apm_accounts/", include("apm_accounts.urls")),
    path("apm_accounts/", include("django.contrib.auth.urls")),
    path("apm_categories/", include("apm_categories.urls")), 
    path("apm_earnings/", include("apm_earnings.urls")),
    path("apm_expenses/", include("apm_expenses.urls")),
    path("ashpensers/", include("ashpensers.urls")),
    path("", include("apm_pages.urls")),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)