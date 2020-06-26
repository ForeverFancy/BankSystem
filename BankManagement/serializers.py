from rest_framework import serializers
from BankManagement.models import *


class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bank
        fields = ('City', 'Bank_Name', 'Asset')


class CheckAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CheckAccount
        fields = ('CAccount_ID', 'CAccount_Balance', 'CAccount_Open_Date',
                  'CAccount_Overdraft', 'CAccount_Open_Bank_Name')


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('Department_ID', 'Department_Manger_ID',
                  'Department_Name', 'Department_Type', 'Bank_Name')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('Employee_ID', 'Employee_Name',
                  'Employee_Phone_Number', 'Employee_Address', 'Employee_Hire_Date', 'Employee_Type', 'Bank_Name', 'Department_ID')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('Customer_ID', 'Customer_Name',
                  'Customer_Phone_Number', 'Customer_Address', 'Contact_Person_Name', 'Contact_Person_Phone_Number', 'Contact_Person_Email', 'Contact_Person_Relationship', 'Employee_ID')


class CustomerToCASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerToCA
        fields = ('CAccount_ID', 'Customer_ID',
                  'CAccount_Open_Bank_Name', 'CAccount_Last_Access_Date')


class LoanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Loan
        fields = ('Loan_ID', 'Loan_Total', 'Loan_Status', 'Bank_Name')


class CustomerToLoanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerToLoan
        fields = ('Customer_ID', 'Loan_ID')


class SavingAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SavingAccount
        fields = ('SAccount_ID', 'SAccount_Balance', 'SAccount_Open_Date',
                  'SAccount_Last_Access_Date', 'SAccount_Interest_Rate', 'SAccount_Currency_Type', 'SAccount_Open_Bank_Name')


class CustomerToSASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerToSA
        fields = ('SAccount_ID', 'Customer_ID',
                  'SAccount_Open_Bank_Name', 'SAccount_Last_Access_Date')


class LoanReleaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoanRelease
        fields = ('Loan_Release_ID', 'Loan_Release_Date',
                  'Loan_Release_Amount')
