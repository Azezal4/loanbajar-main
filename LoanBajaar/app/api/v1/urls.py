from django.contrib import admin
from django.urls import path,re_path,include
from django.http import HttpResponse
# from .views import BankApiView,LoanTypeApiView,LoanApiView
from .views import BankList,BankDetail,LoanTypeList,LoanTypeDetail,LoanList,LoanDetail
app_name    = "app"

def home(request):
    html="<html><body><h1>In API V1</h1></body></html>"
    return HttpResponse(html)

urlpatterns = [
    path('',home),
    # re_path(r'^banks/$',BankApiView.as_view()),
    # re_path(r'^loantypes/$',LoanTypeApiView.as_view()),
    # re_path(r'^loans/$',LoanApiView.as_view()),
    path('banks/', BankList.as_view()),
    path('bank/<pk>', BankDetail.as_view()),
    path('loantypes/', LoanTypeList.as_view()),
    path('loantype/<pk>', LoanTypeDetail.as_view()),
    path('loans/', LoanList.as_view()),
    path('loan/<pk>', LoanDetail.as_view()),
]

