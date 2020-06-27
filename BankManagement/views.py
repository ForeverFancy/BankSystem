from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db import IntegrityError
from BankManagement.models import *
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from BankManagement.serializers import *
import datetime

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


class BankViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class CheckAccountViewSet(viewsets.ModelViewSet):
    '''
    Viewset for check account
    '''
    def list(self, request):
        queryset = CheckAccount.objects.all()
        serializer = CheckAccountSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        checkaccount = request.data.copy()
        checkaccount.pop('Customer_ID')
        checkaccount['CAccount_Open_Date'] = datetime.datetime.now()
        ca_serializer = CheckAccountSerializer(data=checkaccount)

        if ca_serializer.is_valid():
            queryset = Customer.objects.filter(pk=request.data.get('Customer_ID'))
            if not queryset.exists():
                return Response({
                    'status': 'Failed',
                    'message': 'Customer not exist'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            CheckAccount.objects.create(**ca_serializer.validated_data)
            
            ca_to_customer = request.data.copy()
            ca_to_customer.pop('CAccount_Balance')
            ca_to_customer.pop('CAccount_Overdraft')
            ca_to_customer['CAccount_Last_Access_Date'] = datetime.datetime.now()

            ca_to_customer_serializer = CustomerToCASerializer(data=ca_to_customer)
            if ca_to_customer_serializer.is_valid():
                try:
                    CustomerToCA.objects.create(**ca_to_customer_serializer.validated_data)
                except IntegrityError as e:
                    queryset = CheckAccount.objects.all()
                    checkaccount = get_object_or_404(queryset, pk=request.data.get('CAccount_ID'))
                    checkaccount.delete()
                    return Response({
                        'status': 'Bad request',
                        'message': str(e),
                    }, status=status.HTTP_400_BAD_REQUEST)
                return Response({
                    'status': 'Success',
                    'message': 'Create new Check Account Successfully'}, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Invalid data',
        }, status=status.HTTP_400_BAD_REQUEST)


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CustomerViewSet(viewsets.ViewSet):
    '''
    Viewset for customer
    '''
    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        # Testdata: {"Customer_ID": 123456201001010000, "Customer_Name":"Cat", "Customer_Phone_Number": 12345678811, "Customer_Address": "R010", "Contact_Person_Name": "Cas", "Contact_Person_Phone_Number": 12345678810,"Contact_Person_Email": "cat@qq.com", "Contact_Person_Relationship": "Friends", "Employee_ID": 123456199801020001}
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            Customer.objects.create(**serializer.validated_data)
            return Response({
                'status': 'Success',
                'message': 'Create new Customer Successfully'}, status=status.HTTP_201_CREATED)
        
        return Response({
            'status': 'Bad request',
            'message': 'Invalid data',
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # TODO: filter all input query.
    # @action(methods=['get'], url_path='name/(?P<name>\w+)', detail=False)
    # def get_by_name(self, request, name):
    #     print(name)
    #     queryset = Customer.objects.all()
    #     customer = get_object_or_404(queryset, Customer_Name=name)
    #     serializer = CustomerSerializer(customer)
    #     return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Customer.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        queryset = Customer.objects.filter(pk=pk)
        if not queryset.exists():
            return Response({
                'status': 'Failed',
                'message': 'Customer not exist'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        if pk != request.data.get("Customer_ID"):
            return Response({
                'status': 'Failed',
                'message': 'Could not change Customer_ID'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        if not Employee.objects.filter(pk=request.data.get('Employee_ID')).exists():
            return Response({
                'status': 'Failed',
                'message': 'Employee_ID not found'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        queryset.update(
            Customer_Name=request.data.get("Customer_Name"),
            Customer_Phone_Number=request.data.get("Customer_Phone_Number"),
            Customer_Address=request.data.get("Customer_Address"),
            Contact_Person_Name=request.data.get("Contact_Person_Name"),
            Contact_Person_Phone_Number=request.data.get("Contact_Person_Phone_Number"),
            Contact_Person_Email=request.data.get("Contact_Person_Email"),
            Contact_Person_Relationship=request.data.get("Contact_Person_Relationship"),
            Employee_ID=request.data.get("Employee_ID")
        )
        return Response({
            'status': 'Success',
            'message': 'Update data Successfully'}, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = Customer.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        customer.delete()
        return Response({
            'status': 'Success',
            'message': 'Delete data Successfully'}, status=status.HTTP_200_OK)


class CustomerToCAViewSet(viewsets.ModelViewSet):
    queryset = CustomerToCA.objects.all()
    serializer_class = CustomerToCASerializer


class LoanViewSet(viewsets.ViewSet):
    '''
    Viewset for loan.
    '''
    def list(self, request):
        queryset = Loan.objects.all()
        serializer = LoanSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Testdata = {"Loan_ID": "L001", "Loan_Total": 100, "Loan_Status": "0", "Bank_Name":"HF001"}
        serializer = LoanSerializer(data=request.data)

        if serializer.is_valid():
            Loan.objects.create(**serializer.validated_data)
            return Response({
                'status': 'Success',
                'message': 'Create new Loan Successfully'},
                status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({
            'status': 'Bad request',
            'message': 'Invalid data',
        }, status=status.HTTP_400_BAD_REQUEST)


class CustomerToLoanViewSet(viewsets.ModelViewSet):
    queryset = CustomerToLoan.objects.all()
    serializer_class = CustomerToLoanSerializer


class SavingAccountViewSet(viewsets.ModelViewSet):
    '''
    Viewset for saving account
    '''
    def list(self, request):
        queryset = SavingAccount.objects.all()
        serializer = SavingAccountSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        savingaccount = request.data.copy()
        savingaccount.pop('Customer_ID')
        savingaccount['SAccount_Open_Date'] = datetime.datetime.now()
        sa_serializer = SavingAccountSerializer(data=savingaccount)

        if sa_serializer.is_valid():
            queryset = Customer.objects.filter(
                pk=request.data.get('Customer_ID'))
            if not queryset.exists():
                return Response({
                    'status': 'Failed',
                    'message': 'Customer not exist'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            SavingAccount.objects.create(**sa_serializer.validated_data)

            sa_to_customer = request.data.copy()
            sa_to_customer.pop('SAccount_Balance')
            sa_to_customer.pop('SAccount_Interest_Rate')
            sa_to_customer.pop('SAccount_Currency_Type')
            sa_to_customer['SAccount_Last_Access_Date'] = datetime.datetime.now()

            sa_to_customer_serializer = CustomerToSASerializer(
                data=sa_to_customer)
            if sa_to_customer_serializer.is_valid():
                try:
                    CustomerToSA.objects.create(
                    **sa_to_customer_serializer.validated_data)
                except IntegrityError as e:
                    queryset = SavingAccount.objects.all()
                    savingaccount = get_object_or_404(queryset, pk=request.data.get('SAccount_ID'))
                    savingaccount.delete()
                    return Response({
                        'status': 'Bad request',
                        'message': str(e),
                    }, status=status.HTTP_400_BAD_REQUEST)
                return Response({
                    'status': 'Success',
                    'message': 'Create new Saving Account Successfully'}, status=status.HTTP_201_CREATED)
                    
        return Response({
            'status': 'Bad request',
            'message': 'Invalid data',
        }, status=status.HTTP_400_BAD_REQUEST)


class CustomerToSAViewSet(viewsets.ModelViewSet):
    queryset = CustomerToSA.objects.all()
    serializer_class = CustomerToSASerializer


class LoanReleaseViewSet(viewsets.ModelViewSet):
    queryset = LoanRelease.objects.all()
    serializer_class = LoanReleaseSerializer
