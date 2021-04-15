"""

LoanBajaar URL Configuration

"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls',namespace="app")),
    path('api-auth/', include('rest_framework.urls')),
    path('app/',include('app.urls',namespace="app")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns+=[path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)