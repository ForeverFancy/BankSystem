from django.db import models

# Create your models here.


class Bank(models.Model):
    City = models.CharField('City', primary_key=True, max_length=1024)
    Bank_Name = models.CharField('Bank_Name', null=False)
    Asset = models.FloatField('Asset', default=0.0)

    class Meta:
        db_table = 'Bank'


class CheckAccount(models.Model):
    CAccount_ID = models.CharField('CAccount_ID', primary_key=True, max_length=1024)
    CAccount_Balance = models.FloatField('CAccount_Balance', default=0.0)
    CAccount_Open_Date = models.DateTimeField('CAccount_Open_Date')
    CAccount_Overdraft = models.FloatField('CAccount_Overdraft')
    CAccount_Open_Bank_Name = models.ManyToManyField(Customer)  #TODO: FK

    class Meta:
        db_table = 'CheckAccount'


class Department(models.Model):
    Bank_Name = models.ManyToManyField()  #TODO: FK
    Department_ID = models.CharField('Department_ID', max_length=1024)
    Department_Manger_ID = models.CharField('Department_Manger_ID', max_length=18)
    Department_Name = models.CharField('Department_Name', max_length=1024)
    Department_Type = models.IntegerField('Department_Type')
    # TODO: PK

    class Meta:
        db_table = 'Department'


class Employee(models.Model):
    Employee_ID = models.CharField('Employee_ID', max_length=18, null=False, primary_key=True)
    Bank_Name = models.CharField('Bank_Name', max_length=1024, null=False)
    Department_ID = models.CharField('Department_ID', max_length=1024, null=False)
    Employee_Name = models.CharField('Employee_Name', max_length=1024)
    Employee_Phone_Number = models.DecimalField('Employee_Phone_Number', max_digits=11)
    Employee_Address = models.CharField('Employee_Address', max_length=1024)
    Employee_Hire_Date = models.DateTimeField('Employee_Hire_Date')
    Employee_Type = models.IntegerField('Employee_Type')
    # TODO: FK (Bank_Name, Department_ID)

    class Meta:
        db_table = 'Employee'


class Customer(models.Model):
    Customer_ID = models.CharField('Customer_ID', primary_key=True, max_length=18)
    Employee_ID = models.ManyToManyField()  # TODO: FK
    Customer_Name = models.CharField('Customer_Name', max_length=1024)        
    Customer_Phone_Number = models.DecimalField('Customer_Phone_Number', max_digits=11)
    Customer_Address = models.CharField('Customer_Address', max_length=1024)
    Contact_Person_Name = models.CharField('Contact_Person_Name', max_length=1024)
    Contact_Person_Phone_Number = models.DecimalField('Contact_Person_Name', max_digits=11)
    Contact_Person_Email = models.CharField('Contact_Person_Email', max_length=1024)
    Contact_Person_Relationship = models.CharField('Contact_Person_Relationship', max_length=1024)
    # TODO: FK: Employee_ID

    class Meta:
        db_table = 'Customer'


class CustomerToCA(models.Model):
    CAccount_ID = models.CharField('CAccount_ID', max_length=1024)
    Customer_ID = models.CharField('Customer_ID', max_length=18)
    CAccount_Open_Bank_Name = models.CharField('CAccount_Open_Bank_Name', max_length=1024)
    CAccount_Last_Access_Date = models.DateTimeField('CAccount_Last_Access_Date', auto_now=True)
    # TODO: PK: (CAccount_ID, Customer_ID), FK: CAccount_ID, Customer_ID, CAccount_Open_Bank_Name

    class Meta:
        db_table = 'CustomerToCA'


class Loan(models.Model):
    Loan_ID = models.CharField('Loan_ID', max_length=1024, null=False, primary_key=True)
    Bank_Name = models.CharField('Bank_Name', max_length=1024, null=False)
    Loan_Total = models.FloatField('Loan_Total')
    Loan_Status = models.CharField('Loan_Status', max_length=1, default='0')
    #TODO: FK: Bank_Name

    class Meta:
        db_table = 'Loan'


class CustomerToLoan(models.Model):
    Customer_ID = models.CharField('Customer_ID', max_length=18, null=False)
    Loan_ID = models.CharField('Loan_ID', max_length=1024, null=False)
    # TODO: PK: (Customer_ID, Loan_ID), FK: Customer_ID, Loan_ID

    class Meta:
        db_table = 'CustomerToLoan'


class SavingAccount(models.Model):
    SAccount_ID = models.CharField('SAccount_ID', primary_key=True, max_length=1024)
    SAccount_Balance = models.FloatField('SAccount_Balance', default=0.0)
    SAccount_Open_Date = models.DateTimeField('SAccount_Open_Date')
    SAccount_Open_Bank_Name = models.ManyToManyField(Customer)  # TODO: FK
    SAccount_Last_Access_Date = models.DateTimeField('SAccount_Last_Access_Date', auto_now=True)
    SAccount_Interest_Rate = models.FloatField('SAccount_Interest_Rate')
    SAccount_Currency_Type = models.CharField('SAccount_Currency_Type', max_length=1024)
    # TODO: FK: SAccount_Open_Bank_Name

    class Meta:
        db_table = 'SavingAccount'


class CustomerToSA(models.Model):
    SAccount_ID = models.CharField('SAccount_ID', max_length=1024)
    Customer_ID = models.CharField('Customer_ID', max_length=18)
    SAccount_Open_Bank_Name = models.CharField('SAccount_Open_Bank_Name', max_length=1024)
    SAccount_Last_Access_Date = models.DateTimeField('SAccount_Last_Access_Date', auto_now=True)
    # TODO: PK: (CAccount_ID, Customer_ID), FK: CAccount_ID, Customer_ID, CAccount_Open_Bank_Name

    class Meta:
        db_table = 'CustomerToSA'


class LoanRelease(models.Model):
    Loan_ID = models.CharField('Loan_ID', max_length=1024)
    Loan_Release_ID = models.CharField('Loan_Release_ID', max_length=1024)
    Loan_Release_Date = models.DateTimeField('Loan_Release_Date')
    Loan_Release_Amount = models.FloatField('Loan_Release_Amount')
    # TODO: PK: (Loan_ID, Loan_Release_ID), FK: Loan_ID

    class Meta:
        db_table = 'LoanRelease'