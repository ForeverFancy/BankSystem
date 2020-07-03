from django.db import models


MAX_CHAR_LEN = 255


class Bank(models.Model):
    City = models.CharField('City', max_length=MAX_CHAR_LEN)
    Bank_Name = models.CharField('Bank_Name', primary_key=True, blank=False, max_length=MAX_CHAR_LEN)
    Asset = models.FloatField('Asset', default=0.0, blank=False)

    class Meta:
        db_table = 'Bank'


class CheckAccount(models.Model):
    CAccount_ID = models.CharField('CAccount_ID', primary_key=True, max_length=MAX_CHAR_LEN)
    CAccount_Balance = models.DecimalField('CAccount_Balance', max_digits=20, decimal_places=2, blank=False)
    CAccount_Open_Date = models.DateTimeField('CAccount_Open_Date', blank=False)
    CAccount_Overdraft = models.DecimalField('CAccount_Overdraft', max_digits=20, decimal_places=2, blank=False)

    CAccount_Open_Bank_Name = models.ForeignKey(Bank, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CheckAccount'


class Department(models.Model):
    Department_ID = models.CharField('Department_ID', primary_key=True , max_length=MAX_CHAR_LEN, blank=False)
    Department_Manger_ID = models.DecimalField('Department_Manger_ID', max_digits=18, decimal_places=0, blank=False)
    Department_Name = models.CharField('Department_Name', max_length=MAX_CHAR_LEN, blank=False)
    Department_Type = models.IntegerField('Department_Type', blank=False)

    Bank_Name = models.ForeignKey(Bank, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Department'


class Employee(models.Model):
    Employee_ID = models.CharField('Employee_ID', max_length=18, primary_key=True)
    Employee_Name = models.CharField('Employee_Name', max_length=MAX_CHAR_LEN, blank=False)
    Employee_Phone_Number = models.DecimalField('Employee_Phone_Number', max_digits=11, decimal_places=0, blank=False)
    Employee_Address = models.CharField('Employee_Address', max_length=MAX_CHAR_LEN, blank=False)
    Employee_Hire_Date = models.DateTimeField('Employee_Hire_Date', blank=False)
    Employee_Type = models.IntegerField('Employee_Type', blank=False)
    
    Bank_Name = models.ForeignKey(Bank, on_delete=models.CASCADE)
    Department_ID = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Employee'


class Customer(models.Model):
    Customer_ID = models.CharField('Customer_ID', primary_key=True, max_length=18)
    Customer_Name = models.CharField('Customer_Name', max_length=MAX_CHAR_LEN, blank=False)        
    Customer_Phone_Number = models.DecimalField('Customer_Phone_Number', max_digits=11, decimal_places=0, blank=False)
    Customer_Address = models.CharField('Customer_Address', max_length=MAX_CHAR_LEN, blank=False)
    Contact_Person_Name = models.CharField('Contact_Person_Name', max_length=MAX_CHAR_LEN, blank=False)
    Contact_Person_Phone_Number = models.DecimalField('Contact_Person_Name', max_digits=11, decimal_places=0, blank=False)
    Contact_Person_Email = models.CharField('Contact_Person_Email', max_length=MAX_CHAR_LEN, blank=False)
    Contact_Person_Relationship = models.CharField('Contact_Person_Relationship', max_length=MAX_CHAR_LEN, blank=False)

    Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'Customer'


class CustomerToCA(models.Model):
    CAccount_Last_Access_Date = models.DateTimeField('CAccount_Last_Access_Date', auto_now=True)

    CAccount_ID = models.ForeignKey(CheckAccount, on_delete=models.CASCADE)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.PROTECT)
    CAccount_Open_Bank_Name = models.ForeignKey(Bank, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CustomerToCA'
        constraints = [
            models.UniqueConstraint(fields=['Customer_ID', 'CAccount_Open_Bank_Name'], name='One customer is only allowed to open one CA in one bank'),
            models.UniqueConstraint(fields=['CAccount_ID', 'Customer_ID'], name='CustomerToCA Fake Primary Key')
        ]


class Loan(models.Model):
    Loan_ID = models.CharField('Loan_ID', max_length=MAX_CHAR_LEN, blank=False, primary_key=True)
    Loan_Total = models.DecimalField('Loan_Total', max_digits=20, decimal_places=2, blank=False)
    Loan_Status = models.CharField('Loan_Status', max_length=1, default='0')
    
    Bank_Name = models.ForeignKey(Bank, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Loan'


class CustomerToLoan(models.Model):
    Customer_ID = models.ForeignKey(Customer, on_delete=models.PROTECT)
    Loan_ID = models.ForeignKey(Loan, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CustomerToLoan'
        constraints = [
            models.UniqueConstraint(fields=['Loan_ID', 'Customer_ID'], name='Primary key')
        ]
        

class SavingAccount(models.Model):
    SAccount_ID = models.CharField('SAccount_ID', primary_key=True, max_length=MAX_CHAR_LEN)
    SAccount_Balance = models.DecimalField('SAccount_Balance', max_digits=20, decimal_places=2, blank=False)
    SAccount_Open_Date = models.DateTimeField('SAccount_Open_Date', blank=False)
    SAccount_Interest_Rate = models.DecimalField('SAccount_Interest_Rate', max_digits=20, decimal_places=2, blank=False)
    SAccount_Currency_Type = models.CharField('SAccount_Currency_Type', max_length=MAX_CHAR_LEN, blank=False)

    SAccount_Open_Bank_Name = models.ForeignKey(Bank, on_delete=models.CASCADE)

    class Meta:
        db_table = 'SavingAccount'


class CustomerToSA(models.Model):
    SAccount_Last_Access_Date = models.DateTimeField('SAccount_Last_Access_Date', auto_now=True)

    SAccount_ID = models.ForeignKey(SavingAccount, on_delete=models.CASCADE)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.PROTECT)
    SAccount_Open_Bank_Name = models.ForeignKey(Bank, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CustomerToSA'
        constraints = [
            models.UniqueConstraint(fields=['Customer_ID', 'SAccount_Open_Bank_Name'], name='One customer is only allowed to open one SA in one bank'),
            models.UniqueConstraint(fields=['SAccount_ID', 'Customer_ID'], name='CustomerToSA Fake Primary Key')
        ]


class LoanRelease(models.Model):
    Loan_Release_ID = models.CharField('Loan_Release_ID', max_length=MAX_CHAR_LEN, primary_key=True)
    Loan_Release_Date = models.DateTimeField('Loan_Release_Date', blank=False)
    Loan_Release_Amount = models.DecimalField('Loan_Release_Amount', max_digits=20, decimal_places=2, blank=False)

    Loan_ID = models.ForeignKey(Loan, on_delete=models.CASCADE)

    class Meta:
        db_table = 'LoanRelease'
        constraints = [
            models.UniqueConstraint(fields=['Loan_ID', 'Loan_Release_ID'], name='LoanRelease Fake Primary Key')
        ]
