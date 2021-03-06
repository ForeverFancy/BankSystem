from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db import IntegrityError, transaction
from django.db.models import ProtectedError
from BankManagement.models import *
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from BankManagement.serializers import *
from rest_framework.permissions import AllowAny
import datetime
import json

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
    permission_classes = (AllowAny,)
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class CheckAccountViewSet(viewsets.ModelViewSet):
    '''
    Viewset for check account
    '''
    permission_classes = (AllowAny,)

    def list(self, request):
        queryset = CheckAccount.objects.all()
        serializer = CheckAccountSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @transaction.atomic
    def create(self, request):
        checkaccount = request.data.copy()
        
        try:
            checkaccount.pop('Customer_ID')
        except KeyError as e:
            return Response({
                'status': 'Failed',
                'message': 'Customer_ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        ca_to_customer = request.data.copy()
        
        try:
            ca_to_customer.pop('CAccount_Balance')
            ca_to_customer.pop('CAccount_Overdraft')
        except KeyError as e:
            return Response({
                'status': 'Failed',
                'message': 'More information is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Customer.objects.filter(pk=request.data.get('Customer_ID'))
        if not queryset.exists():
            return Response({
                'status': 'Failed',
                'message': 'Customer not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            with transaction.atomic():
                checkaccount['CAccount_Open_Date'] = datetime.datetime.now()
                ca_serializer = CheckAccountSerializer(data=checkaccount)

                if ca_serializer.is_valid():
                    CheckAccount.objects.create(**ca_serializer.validated_data)

                    ca_to_customer['CAccount_Last_Access_Date'] = datetime.datetime.now()

                    ca_to_customer_serializer = CustomerToCASerializer(data=ca_to_customer)
                    if ca_to_customer_serializer.is_valid():
                        CustomerToCA.objects.create(**ca_to_customer_serializer.validated_data)
                        # except IntegrityError as e:
                        #     queryset = CheckAccount.objects.all()
                        #     checkaccount = get_object_or_404(queryset, pk=request.data.get('CAccount_ID'))
                        #     checkaccount.delete()
                        #     return Response({
                        #         'status': 'Bad request',
                        #         'message': str(e),
                        #     }, status=status.HTTP_400_BAD_REQUEST)
                        
        except IntegrityError as e:
            return Response({
                'status': 'Bad request',
                'message': str(e),
                }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'status': 'Success',
            'message': 'Create new Check Account Successfully'}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = CheckAccount.objects.all()
        checkaccount = get_object_or_404(queryset, pk=pk)
        serializer = CheckAccountSerializer(checkaccount)
        return Response(serializer.data)

    @transaction.atomic
    def update(self, request, pk=None):
        # Only balance and overdraft are allowed to modify
        queryset = CheckAccount.objects.filter(pk=pk)
        if not queryset.exists():
            return Response({
                'status': 'Failed',
                'message': 'Check Account not exist'}, status=status.HTTP_400_BAD_REQUEST)
        if pk != request.data.get("CAccount_ID"):
            return Response({
                'status': 'Failed',
                'message': 'Could not change CAccount_ID'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            with transaction.atomic():
                queryset.update(
                    CAccount_ID=pk,
                    CAccount_Balance=request.data.get('CAccount_Balance') if request.data.get('CAccount_Balance') else queryset[0].CAccount_Balance,
                    CAccount_Overdraft=request.data.get('CAccount_Overdraft') if request.data.get('CAccount_Overdraft') else queryset[0].CAccount_Overdraft,
                )
                queryset = CustomerToCA.objects.filter(CAccount_ID=pk)
                queryset.update(
                    CAccount_Last_Access_Date=datetime.datetime.now()
                )
        except IntegrityError as e:
            return Response({
                'status': 'Bad request',
                'message': str(e),
            }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            'status': 'Success',
            'message': 'Update Check Account Successfully'}, status=status.HTTP_200_OK)

    @transaction.atomic
    def destroy(self, request, pk=None):
        queryset = CheckAccount.objects.all()
        checkaccount = get_object_or_404(queryset, pk=pk)
        queryset = CustomerToCA.objects.all()
        customer_to_ca = get_list_or_404(queryset, CAccount_ID=pk)
        try:
            with transaction.atomic():
                for obj in customer_to_ca:
                    obj.delete()
                checkaccount.delete()
            return Response({
            'status': 'Success',
            'message': 'Delete Check Account Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError as e:
            return Response({
                'status': 'Bad request',
                'message': str(e),
            }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            'status': 'Success',
            'message': 'Delete Check Account Successfully'}, status=status.HTTP_200_OK)


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CustomerViewSet(viewsets.ViewSet):
    '''
    Viewset for customer
    '''
    permission_classes = (AllowAny,)

    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
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

    def retrieve(self, request, pk=None):
        queryset = Customer.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    @transaction.atomic
    def update(self, request, pk=None):
        queryset = Customer.objects.filter(pk=pk)
        if not queryset.exists():
            return Response({
                'status': 'Failed',
                'message': 'Customer not exist'}, status=status.HTTP_400_BAD_REQUEST)
        if pk != request.data.get("Customer_ID"):
            return Response({
                'status': 'Failed',
                'message': 'Could not change Customer_ID'}, status=status.HTTP_400_BAD_REQUEST)
        if request.data.get('Employee_ID') and not Employee.objects.filter(pk=request.data.get('Employee_ID')).exists():
            return Response({
                'status': 'Failed',
                'message': 'Employee_ID not found'}, status=status.HTTP_400_BAD_REQUEST)
        with transaction.atomic():
            queryset.update(
                Customer_Name=request.data.get("Customer_Name") if request.data.get("Customer_Name") else queryset[0].Customer_Name,
                Customer_Phone_Number=request.data.get("Customer_Phone_Number") if request.data.get("Customer_Phone_Number") else queryset[0].Customer_Phone_Number,
                Customer_Address=request.data.get("Customer_Address") if request.data.get("Customer_Address") else queryset[0].Customer_Address,
                Contact_Person_Name=request.data.get("Contact_Person_Name") if request.data.get("Contact_Person_Name") else queryset[0].Contact_Person_Name,
                Contact_Person_Phone_Number=request.data.get("Contact_Person_Phone_Number") if request.data.get("Contact_Person_Phone_Number") else queryset[0].    Contact_Person_Phone_Number,
                Contact_Person_Email=request.data.get("Contact_Person_Email") if request.data.get("Contact_Person_Email") else queryset[0].Contact_Person_Email,
                Contact_Person_Relationship=request.data.get("Contact_Person_Relationship") if request.data.get("Contact_Person_Relationship") else queryset[0].    Contact_Person_Relationship,
                Employee_ID=request.data.get("Employee_ID") if request.data.get("Employee_ID") else queryset[0].Employee_ID
            )
        return Response({
            'status': 'Success',
            'message': 'Update data Successfully'}, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = Customer.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        try:
            customer.delete()
        except ProtectedError as e:
            return Response({
                'status': 'Failed',
                'message': 'Could not delete'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'status': 'Success',
            'message': 'Delete data Successfully'}, status=status.HTTP_200_OK)


class CustomerToCAViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = CustomerToCA.objects.all()
    serializer_class = CustomerToCASerializer


class LoanViewSet(viewsets.ViewSet):
    '''
    Viewset for loan.
    '''
    permission_classes = (AllowAny,)

    def list(self, request):
        queryset = Loan.objects.all()
        serializer = LoanSerializer(queryset, many=True)
        return Response(serializer.data)

    @transaction.atomic
    def create(self, request):
        loan = request.data.copy()
        try:
            loan.pop('Customer_ID')
        except KeyError as e:
            return Response({
                'status': 'Failed',
                'message': 'Customer_ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        customer_to_loan = request.data.copy()
        try:
            customer_to_loan.pop('Loan_Total')
            customer_to_loan.pop('Loan_Status')
            customer_to_loan.pop('Bank_Name')
        except KeyError as e:
            return Response({
                'status': 'Failed',
                'message': 'More information is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Customer.objects.filter(pk=request.data.get('Customer_ID'))
        if not queryset.exists():
            return Response({
                'status': 'Failed',
                'message': 'Customer not exist'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = LoanSerializer(data=request.data)

        try:
            with transaction.atomic():
                if serializer.is_valid():
                    Loan.objects.create(**serializer.validated_data)
                    customer_to_loan_serializer = CustomerToLoanSerializer(data=customer_to_loan)
                if customer_to_loan_serializer.is_valid():
                    CustomerToLoan.objects.create(**customer_to_loan_serializer.validated_data)
        except IntegrityError as e:
            return Response({
                'status': 'Bad request',
                'message': str(e),
            }, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({
            'status': 'Success',
            'message': 'Create new Loan Successfully'},
            status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        return Response({
            'status': 'Bad request',
            'message': 'Loan is not allowed to modify',
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Loan.objects.all()
        loan = get_object_or_404(queryset, pk=pk)
        serializer = LoanSerializer(loan)
        return Response(serializer.data)
    
    @transaction.atomic
    def destroy(self, request, pk=None):
        queryset = Loan.objects.all()
        loan = get_object_or_404(queryset, pk=pk)
        queryset = CustomerToLoan.objects.all()
        customer_to_loan = get_list_or_404(queryset, Loan_ID=pk)
        if loan.Loan_Status == '1':
            return Response({
                'status': 'Bad request',
                'message': 'A loan record in the issuing state is not allowed to be deleted',
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            with transaction.atomic():
                for obj in customer_to_loan:
                    obj.delete()
                loan.delete()
        except IntegrityError as e:
            return Response({
                'status': 'Bad request',
                'message': str(e),
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'status': 'Success',
            'message': 'Delete Loan Successfully'}, status=status.HTTP_200_OK)


class CustomerToLoanViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = CustomerToLoan.objects.all()
    serializer_class = CustomerToLoanSerializer


class SavingAccountViewSet(viewsets.ViewSet):
    '''
    Viewset for saving account
    '''
    permission_classes = (AllowAny,)

    def list(self, request):
        queryset = SavingAccount.objects.all()
        serializer = SavingAccountSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        savingaccount = request.data.copy()

        try:
            savingaccount.pop('Customer_ID')
        except KeyError as e:
            return Response({
                'status': 'Failed',
                'message': 'Customer_ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            sa_to_customer = request.data.copy()
            sa_to_customer.pop('SAccount_Balance')
            sa_to_customer.pop('SAccount_Interest_Rate')
            sa_to_customer.pop('SAccount_Currency_Type')
        except KeyError as e:
            return Response({
                'status': 'Failed',
                'message': 'More information is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Customer.objects.filter(
            pk=request.data.get('Customer_ID'))
        if not queryset.exists():
            return Response({
                'status': 'Failed',
                'message': 'Customer not exist'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        savingaccount['SAccount_Open_Date'] = datetime.datetime.now()
        sa_serializer = SavingAccountSerializer(data=savingaccount)

        try:
            with transaction.atomic():
                if sa_serializer.is_valid():
                    SavingAccount.objects.create(**sa_serializer.validated_data)
                    sa_to_customer['SAccount_Last_Access_Date'] = datetime.datetime.now()

                    sa_to_customer_serializer = CustomerToSASerializer(
                        data=sa_to_customer)
                    if sa_to_customer_serializer.is_valid():
                        CustomerToSA.objects.create(
                        **sa_to_customer_serializer.validated_data)
        except IntegrityError as e:
            return Response({
                'status': 'Bad request',
                'message': str(e),
            }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            'status': 'Success',
            'message': 'Create new Saving Account Successfully'}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = SavingAccount.objects.all()
        savingaccount = get_object_or_404(queryset, pk=pk)
        serializer = SavingAccountSerializer(savingaccount)
        return Response(serializer.data)
    
    @transaction.atomic
    def update(self, request, pk=None):
        # Only balance and overdraft are allowed to modify
        queryset = SavingAccount.objects.filter(pk=pk)
        if not queryset.exists():
            return Response({
                'status': 'Failed',
                'message': 'Check Account not exist'}, status=status.HTTP_400_BAD_REQUEST)
        if pk != request.data.get("SAccount_ID"):
            return Response({
                'status': 'Failed',
                'message': 'Could not change SAccount_ID'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            with transaction.atomic():
                queryset.update(
                    SAccount_ID=pk,
                    SAccount_Balance=request.data.get('SAccount_Balance') if request.data.get('SAccount_Balance') else queryset[0].SAccount_Balance,
                    SAccount_Interest_Rate=request.data.get('SAccount_Interest_Rate') if request.data.get('SAccount_Interest_Rate') else queryset[0].SAccount_Interest_Rate,
                    SAccount_Currency_Type=request.data.get('SAccount_Currency_Type') if request.data.get('SAccount_Currency_Type') else queryset[0].SAccount_Currency_Type,
                )
                queryset = CustomerToSA.objects.filter(SAccount_ID=pk)
                queryset.update(
                    SAccount_Last_Access_Date=datetime.datetime.now()
                )
        except IntegrityError as e:
            return Response({
                'status': 'Bad request',
                'message': str(e),
            }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            'status': 'Success',
            'message': 'Update Check Account Successfully'}, status=status.HTTP_200_OK)
    
    @transaction.atomic
    def destroy(self, request, pk=None):
        queryset = SavingAccount.objects.all()
        savingaccount = get_object_or_404(queryset, pk=pk)
        queryset = CustomerToSA.objects.all()
        customer_to_sa = get_list_or_404(queryset, SAccount_ID=pk)
        try:
            with transaction.atomic():
                for obj in customer_to_sa:
                    obj.delete()
                savingaccount.delete()
        except IntegrityError as e:
            return Response({
                'status': 'Bad request',
                'message': str(e),
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'status': 'Success',
            'message': 'Delete Saving Account Successfully'}, status=status.HTTP_200_OK)


class CustomerToSAViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = CustomerToSA.objects.all()
    serializer_class = CustomerToSASerializer


class LoanReleaseViewSet(viewsets.ViewSet):
    '''
    Viewset for loan release
    '''
    permission_classes = (AllowAny,)
    
    def list(self, request):
        queryset = LoanRelease.objects.all()
        serializer = LoanReleaseSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @transaction.atomic
    def create(self, request):
        loan_id = request.data.get('Loan_ID')
        loan = Loan.objects.filter(pk=request.data.get('Loan_ID'))
        
        if not loan.exists():
            return Response({
                'status': 'Failed',
                'message': 'Loan not exist'}, status=status.HTTP_400_BAD_REQUEST)
    
        if loan.get().Loan_Status == '2':
            return Response({
                'status': 'Failed',
                'message': 'Loan is finished'}, status=status.HTTP_400_BAD_REQUEST)

        queryset = LoanRelease.objects.filter(Loan_ID=request.data.get('Loan_ID'))
        loan_amount = sum([q.Loan_Release_Amount for q in queryset])

        if float(loan_amount) + float(request.data.get('Loan_Release_Amount')) > float(loan.get().Loan_Total):
            return Response({
                'status': 'Failed',
                'message': 'Loan release is more than total amount'}, status=status.HTTP_400_BAD_REQUEST)
        newrequest = request.data.copy()
        newrequest['Loan_Release_Date'] = datetime.datetime.now()
        serializer = LoanReleaseSerializer(data=newrequest)
        
        try:
            with transaction.atomic():
                if serializer.is_valid():
                    LoanRelease.objects.create(**serializer.validated_data)
                    queryset = Loan.objects.filter(pk=request.data.get('Loan_ID'))
                    if float(loan_amount) + float(request.data.get('Loan_Release_Amount')) == float(loan.get().Loan_Total):
                        queryset.update(Loan_Status='2')
                    else:
                        queryset.update(Loan_Status='1')
        except IntegrityError as e:       
            return Response({
                'status': 'Bad request',
                'message': 'Invalid data',
            }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            'status': 'Success',
            'message': 'Create new Loan Release Successfully'},
            status=status.HTTP_201_CREATED)
        
    
    def retrieve(self, request, pk=None):
        queryset = LoanRelease.objects.all()
        loan = get_object_or_404(queryset, Loan_Release_ID=pk)
        serializer = LoanReleaseSerializer(loan)
        return Response(serializer.data)

    def update(self, request, pk=None):
        return Response({
            'status': 'Bad request',
            'message': 'Loan Release is not allowed to modify',
        }, status=status.HTTP_400_BAD_REQUEST)
    
    @transaction.atomic
    def destroy(self, request, pk=None):
        queryset = LoanRelease.objects.all()
        loan_release = get_object_or_404(queryset, pk=pk)
        loan = loan_release.Loan_ID

        if loan.Loan_Status == '1':
            return Response({
                'status': 'Bad request',
                'message': 'A loan release record in the issuing state is not allowed to be deleted',
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            with transaction.atomic():
                loan_release.delete()
                queryset = LoanRelease.objects.filter(Loan_ID=loan)
                if not queryset.exists():
                    queryset.update(Loan_Status='0')
                else:
                    loan_amount = sum([q.Loan_Release_Amount for q in queryset])
                    if float(loan_amount) == float(loan.get().Loan_Total):
                        queryset.update(Loan_Status='2')
                    elif float(loan_amount) == 0:
                        queryset.update(Loan_Status='0')
                    else:
                        queryset.update(Loan_Status='1')
        except IntegrityError as e:
            return Response({
                'status': 'Bad request',
                'message': str(e),
            }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            'status': 'Success',
            'message': 'Delete Loan Release Successfully'}, status=status.HTTP_200_OK)


class StatisticalDataViewSet(viewsets.ViewSet):
    '''
    Viewset for statistical data
    '''
    permission_classes = (AllowAny,)

    def list(self, request):
        bank_set = Bank.objects.all()
        time_list = []
        for bank in bank_set:
            saving_account_set = SavingAccount.objects.filter(SAccount_Open_Bank_Name=bank.Bank_Name)
            overall_balance = 0.00
            for sa in saving_account_set:
                time_list.append(sa.SAccount_Open_Date)
                overall_balance += float(sa.SAccount_Balance)
        start_time = min(time_list)
        now_time = datetime.datetime.now()

        # Process year
        bank_year_data = []
        bank_quarter_data = []
        bank_month_data = []
        quarter_range = [[1, 3], [4, 6], [7, 9], [10, 12]]
        for bank in bank_set:
            tmp = {}
            for year in range(start_time.year, now_time.year + 1):
                saving_account_set = SavingAccount.objects.filter(
                    SAccount_Open_Bank_Name=bank.Bank_Name)
                loan_set = Loan.objects.filter(
                        Bank_Name=bank.Bank_Name)
                overall_balance = 0.00
                overall_loan = 0.00
                overall_customer = 0
                for sa in saving_account_set:
                    if sa.SAccount_Open_Date.year <= year:
                        overall_balance += float(sa.SAccount_Balance)
                        overall_customer += 1
                for ln in loan_set:
                    release_set = LoanRelease.objects.filter(Loan_ID=ln.Loan_ID)
                    for release in release_set:
                        if release.Loan_Release_Date.year <= year:
                            overall_loan += float(release.Loan_Release_Amount)
                tmp[str(year)] = [overall_balance, overall_loan, overall_customer]
            bank_year_data.append(tmp)
        # print(bank_year_data)

        # Process quarter
        for bank in bank_set:
            tmp = {}
            for year in range(start_time.year, now_time.year + 1):
                for quarter in range(1, 5):
                    saving_account_set = SavingAccount.objects.filter(
                        SAccount_Open_Bank_Name=bank.Bank_Name)
                    loan_set = Loan.objects.filter(
                        Bank_Name=bank.Bank_Name)
                    overall_balance = 0.00
                    overall_loan = 0.00
                    overall_customer = 0
                    for sa in saving_account_set:
                        if sa.SAccount_Open_Date.year <= year and quarter_range[quarter-1][0] <= sa.SAccount_Open_Date.month <= quarter_range [quarter-1][1]:
                            overall_balance += float(sa.SAccount_Balance)
                            overall_customer += 1
                    for ln in loan_set:
                        release_set = LoanRelease.objects.filter(Loan_ID=ln.Loan_ID)
                        for release in release_set:
                            if release.Loan_Release_Date.year <= year and quarter_range[quarter-1][0] <= release.Loan_Release_Date.month <= quarter_range [quarter-1][1]:
                                overall_loan += float(release.Loan_Release_Amount)
                    tmp[str(year) + "-Q" + str(quarter)] = [overall_balance, overall_loan, overall_customer]
            bank_quarter_data.append(tmp)
        # print(bank_quarter_data)

        # Process month
        for bank in bank_set:
            tmp = {}
            for year in range(start_time.year, now_time.year + 1):
                for month in range(1, datetime.datetime.now().month + 1):
                    saving_account_set = SavingAccount.objects.filter(
                        SAccount_Open_Bank_Name=bank.Bank_Name)
                    loan_set = Loan.objects.filter(
                        Bank_Name=bank.Bank_Name)
                    overall_balance = 0.00
                    overall_loan = 0.00
                    overall_customer = 0
                    for sa in saving_account_set:
                        if sa.SAccount_Open_Date.year <= year and sa.SAccount_Open_Date.month == month:
                            overall_balance += float(sa.SAccount_Balance)
                            overall_customer += 1
                    for ln in loan_set:
                        release_set = LoanRelease.objects.filter(Loan_ID=ln.Loan_ID)
                        for release in release_set:
                            if release.Loan_Release_Date.year <= year and release.Loan_Release_Date.month == month:
                                overall_loan += float(release.Loan_Release_Amount)
                    tmp[str(year) + "-M" + str(month)] = [overall_balance, overall_loan, overall_customer]
            bank_month_data.append(tmp)
        # print(bank_month_data)

        response_data = {}
        response_data['year_data'] = bank_year_data
        response_data['quarter_data'] = bank_quarter_data
        response_data['month_data'] = bank_month_data

        return Response(response_data)
