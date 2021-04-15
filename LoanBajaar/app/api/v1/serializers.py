from rest_framework import serializers
from app.models import Bank,LoanType,Loan

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = [
            'id',
            "name", 
            "contact_numbers", 
            "branches", 
            "active", 
            "updatedDate"
            ]

class LoanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanType
        fields = [
            "id",
            "loan_type",
            "updatedDate"
            ]

class LoanSerializer(serializers.ModelSerializer):
    bank        = serializers.StringRelatedField(many=False)
    loan_type   = serializers.StringRelatedField(many=False)
    class Meta:
        model = Loan
        fields = [
            "id",
            "loan_name",
            "loan_type",
            "bank",
            "branch",
            "interest_rate",
            "min_term",
            "max_term",
            "min_loan_amount",
            "max_loan_amount",
            "min_annual_income",
            "min_age",
            "max_age",
            "active", 
            "updatedDate"
            ]