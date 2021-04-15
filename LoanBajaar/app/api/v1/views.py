from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from app.models import Bank,LoanType,Loan
from .serializers import BankSerializer,LoanTypeSerializer,LoanSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

class BankList(ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankDetail(RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class LoanTypeList(ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = LoanType.objects.all()
    serializer_class = LoanTypeSerializer

class LoanTypeDetail(RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = LoanType.objects.all()
    serializer_class = LoanTypeSerializer

class LoanList(ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LoanSerializer
    
    def get_queryset(self):
        queryset        = Loan.objects.all()
        term            = self.request.query_params.get('term')
        annual_income   = self.request.query_params.get('annual_income')
        interest_rate   = self.request.query_params.get('interest_rate')
        bank            = self.request.query_params.get('bank_name')
        loan_type       = self.request.query_params.get('loan_type')
        age             = self.request.query_params.get('age')
        loan_amount     = self.request.query_params.get('loan_amount')

        try:
            if term:
                queryset = queryset.filter(min_term__lte=term,max_term__gte=term)
        except:pass

        try:
            if annual_income:
                queryset = queryset.filter(min_annual_income__lte=annual_income)
        except:pass

        try:
            if interest_rate:
                queryset = queryset.filter(interest_rate__lte=interest_rate)
        except:pass

        try:
            if bank:
                if bank[0]=="\"":
                    bank = bank[1:-1]
                queryset = queryset.filter(bank__name=bank)
        except:pass

        try:
            if loan_type:
                if loan_type[0]=="\"":
                    loan_type = loan_type[1:-1]
                queryset = queryset.filter(loan_type__loan_type=loan_type)
        except:pass

        try:
            if age:
                queryset = queryset.filter(min_age__lte=age,max_age__gte=age)
        except:pass

        try:
            if loan_amount:
                queryset = queryset.filter(min_loan_amount__lte=term,max_loan_amount__gte=term)
        except:pass

        return queryset
    

class LoanDetail(RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

# class BankApiView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]

#     # 1. List all
#     def get(self, request, *args, **kwargs):
#         '''
#         List all the banks
#         '''
#         if(request.data.get('id')):
#             bank = Bank.objects.get(id=request.data.get('id'))
#             serializer = BankSerializer(bank)
#         else:
#             banks = Bank.objects.all()
#             serializer = BankSerializer(banks,many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 2. Create
#     def post(self, request, *args, **kwargs):
#         '''
#         Create the Bank with given bank data
#         '''
#         data = {
#             'name': request.data.get('name'), 
#             'contact_numbers': request.data.get('contact_numbers'), 
#             'branches': request.data.get('branches')
#         }
#         serializer = BankSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoanTypeApiView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]

#     # 1. List all
#     def get(self, request, *args, **kwargs):
#         '''
#         List all the loan types
#         '''
#         loantypes = LoanType.objects.all()
#         serializer = LoanTypeSerializer(loantypes, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 2. Create
#     def post(self, request, *args, **kwargs):
#         '''
#         Create the new loan Type
#         '''
#         data = {
#             'name': request.data.get('name'), 
#         }
#         serializer = LoanTypeSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoanApiView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]

#     # 1. List all
#     def get(self, request, *args, **kwargs):
#         '''
#         List all the loans
#         '''
#         if(request.data.get('id')):
#             loan = Bank.objects.get(id=request.data.get('id'))
#             serializer = LoanSerializer(loan)
#         else:
#             loans = Loan.objects.all()
#             serializer = LoanSerializer(loans,many=True)
        
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 2. Create
#     def post(self, request, *args, **kwargs):
#         '''
#         Create the Loan with given data
#         '''
#         data = {
#             'name': request.data.get('name'), 
#             'contact_numbers': request.data.get('contact_numbers'), 
#             'branches': request.data.get('branches')
#         }
#         serializer = LoanSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)