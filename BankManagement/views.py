from django.shortcuts import render
from django.http import HttpResponse
from BankManagement.models import *
from rest_framework import viewsets
from BankManagement.serializers import *

# Create your views here.

def init(request):
    bank = Bank(City='Hefei', Bank_Name='HF001', Asset=12578.3)
    bank.save()
    department = Department(Department_ID='DP001', Department_Manger_ID=123456199901010001, Department_Name='Sale', Department_Type=0, Bank_Name=bank)
    department.save()
    employee = Employee(Employee_ID=123456199801020001, Employee_Name='Emy', Employee_Phone_Number=12345678910, Employee_Address='R001', Employee_Hire_Date='2019-01-01', Employee_Type=1, Bank_Name=bank, Department_ID=department)
    employee.save()

    bank = Bank(City='Hefei', Bank_Name='HF002', Asset=32479.29)
    bank.save()
    department = Department(Department_ID='DP002', Department_Manger_ID=123456199901010002, Department_Name='Finance', Department_Type=1, Bank_Name=bank)
    department.save()
    employee = Employee(Employee_ID=123456199801020002, Employee_Name='Emma', Employee_Phone_Number=12345678911, Employee_Address='R001', Employee_Hire_Date='2019-02-01', Employee_Type=1, Bank_Name=bank, Department_ID=department)
    employee.save()
    
    bank = Bank(City='Hefei', Bank_Name='HF003', Asset=4316421.36)
    bank.save()
    department = Department(Department_ID='DP003', Department_Manger_ID=123456199901010003, Department_Name='Sale', Department_Type=0, Bank_Name=bank)
    department.save()
    employee = Employee(Employee_ID=123456199801020003, Employee_Name='Emde', Employee_Phone_Number=12345678912, Employee_Address='R001', Employee_Hire_Date='2019-05-01', Employee_Type=1, Bank_Name=bank, Department_ID=department)
    employee.save()
    
    bank = Bank(City='Hefei', Bank_Name='HF004', Asset=234852734.3)
    bank.save()
    department = Department(Department_ID='DP004', Department_Manger_ID=123456199901010004, Department_Name='Mangement', Department_Type=2, Bank_Name=bank)
    department.save()
    employee = Employee(Employee_ID=123456199801020004, Employee_Name='Eym', Employee_Phone_Number=12345678913, Employee_Address='R001', Employee_Hire_Date='2017-01-01', Employee_Type=1, Bank_Name=bank, Department_ID=department)
    employee.save()
    
    bank = Bank(City='Hefei', Bank_Name='HF005', Asset=3494752.3)
    bank.save()
    department = Department(Department_ID='DP005', Department_Manger_ID=123456199901010005, Department_Name='Sale', Department_Type=0, Bank_Name=bank)
    department.save()
    employee = Employee(Employee_ID=123456199801020005, Employee_Name='Eld', Employee_Phone_Number=12345678914, Employee_Address='R001', Employee_Hire_Date='2018-01-01', Employee_Type=1, Bank_Name=bank, Department_ID=department)
    employee.save()

    return HttpResponse("Finish init.")


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class CheckAccountViewSet(viewsets.ModelViewSet):
    queryset = CheckAccount.objects.all()
    serializer_class = CheckAccountSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerToCAViewSet(viewsets.ModelViewSet):
    queryset = CustomerToCA.objects.all()
    serializer_class = CustomerToCASerializer


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class CustomerToLoanViewSet(viewsets.ModelViewSet):
    queryset = CustomerToLoan.objects.all()
    serializer_class = CustomerToLoanSerializer


class SavingAccountViewSet(viewsets.ModelViewSet):
    queryset = SavingAccount.objects.all()
    serializer_class = SavingAccountSerializer


class CustomerToSAViewSet(viewsets.ModelViewSet):
    queryset = CustomerToSA.objects.all()
    serializer_class = CustomerToSASerializer


class LoanReleaseViewSet(viewsets.ModelViewSet):
    queryset = LoanRelease.objects.all()
    serializer_class = LoanReleaseSerializer
