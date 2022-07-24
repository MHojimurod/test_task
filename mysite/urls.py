"""mysite URL Configuration

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
from django.shortcuts import render
from django.urls import path, include,re_path
from rest_framework import permissions
#Libraries for api scheme interface
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("myapp.urls")),
    # re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

]

#API scheme  interface
schema_view = get_schema_view(
    openapi.Info(
        title="Test Task API Scheme",
        default_version='v1',
        description="API TESTING",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


def home(request):
    return render(request, 'index.html')


urlpatterns += [
                path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                path('', home), path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
            ]


urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)