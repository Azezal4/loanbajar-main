from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField

app_name    = "app"

class Uuid(models.Model):
    id              = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )

    @property
    def pk(self):
        return str(self.id)

    class Meta:
        abstract    = True

class Timestamp(models.Model):
    createdDate     = models.DateTimeField(auto_now_add=True)
    updatedDate     = models.DateTimeField(auto_now=True)
    active          = models.BooleanField(verbose_name=("active"), default=True)

    class Meta:
        abstract = True


class UUidTimestamp(Uuid, Timestamp):
    class Meta:
        abstract = True


class Bank(UUidTimestamp):
    name                = models.CharField(max_length=255, verbose_name=("bank name"))
    contact_numbers     = ArrayField(models.CharField(max_length=200), blank=True,null=True)
    branches            = ArrayField(models.CharField(max_length=200), blank=True,null=True)

    class Meta:
        verbose_name        = "Bank"
        verbose_name_plural = "Banks"
        ordering            = ["name"]

    def __str__(self) -> str:
        return str(self.name)

    def get_all_loans(self):
        return Loan.objects.filter(bank=self)


class LoanType(UUidTimestamp):
    loan_type           = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.loan_type)

class Loan(UUidTimestamp):

    #Bank Details
    bank                = models.ForeignKey(Bank,on_delete=models.CASCADE)
    branch              = models.CharField(max_length=10)

    #Loan Details
    loan_name           = models.CharField(max_length=255, verbose_name=("loan name"))
    loan_type           = models.ForeignKey(LoanType,on_delete=models.CASCADE)
    interest_rate       = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=("interest rate"))
    #LOAN DESCRIPTION 
    
    #Requirement Details
    min_term            = models.IntegerField(verbose_name=("minimum term"))
    max_term            = models.IntegerField(verbose_name=("maximum term"))
    min_loan_amount     = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=("minimum loan amount"))
    max_loan_amount     = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=("maximum loan amount"))
    min_annual_income   = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=("minimum annual income"))
    min_age             = models.IntegerField(verbose_name=("minimum age"))
    max_age             = models.IntegerField(verbose_name=("maximum age"))

    class Meta:
        verbose_name        = "Loan"
        verbose_name_plural = "Loans"
        ordering            = ["loan_name"]

    def __str__(self) -> str:
        return str(self.loan_name)


