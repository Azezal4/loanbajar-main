"""

LoanBajaar/app URL Configuration

"""

from django.contrib import admin
from django.urls import path,re_path,include
from django.http import HttpResponse


app_name    = "app"

urlpatterns = [
    path('',include('app.api.urls')),
    path('api/',include('app.api.urls'))
]