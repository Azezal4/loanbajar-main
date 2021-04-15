"""

LoanBajaar/app/api URL Configuration

"""

from django.contrib import admin
from django.urls import path,re_path,include
from django.http import HttpResponse


app_name    = "app"

def home(request):
    html="<html><body><h1>In API</h1></body></html>"
    return HttpResponse(html)

urlpatterns = [
    path('',home),
    path('v1/',include('app.api.v1.urls'))
]