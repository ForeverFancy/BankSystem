# Generated by Django 3.0.7 on 2020-06-26 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('City', models.CharField(max_length=255, verbose_name='City')),
                ('Bank_Name', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Bank_Name')),
                ('Asset', models.FloatField(default=0.0, verbose_name='Asset')),
            ],
            options={
                'db_table': 'Bank',
            },
        ),
        migrations.CreateModel(
            name='CheckAccount',
            fields=[
                ('CAccount_ID', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='CAccount_ID')),
                ('CAccount_Balance', models.FloatField(default=0.0, verbose_name='CAccount_Balance')),
                ('CAccount_Open_Date', models.DateTimeField(verbose_name='CAccount_Open_Date')),
                ('CAccount_Overdraft', models.FloatField(verbose_name='CAccount_Overdraft')),
                ('CAccount_Open_Bank_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.Bank')),
            ],
            options={
                'db_table': 'CheckAccount',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Customer_ID', models.CharField(max_length=18, primary_key=True, serialize=False, verbose_name='Customer_ID')),
                ('Customer_Name', models.CharField(max_length=255, verbose_name='Customer_Name')),
                ('Customer_Phone_Number', models.DecimalField(decimal_places=0, max_digits=11, verbose_name='Customer_Phone_Number')),
                ('Customer_Address', models.CharField(max_length=255, verbose_name='Customer_Address')),
                ('Contact_Person_Name', models.CharField(max_length=255, verbose_name='Contact_Person_Name')),
                ('Contact_Person_Phone_Number', models.DecimalField(decimal_places=0, max_digits=11, verbose_name='Contact_Person_Name')),
                ('Contact_Person_Email', models.CharField(max_length=255, verbose_name='Contact_Person_Email')),
                ('Contact_Person_Relationship', models.CharField(max_length=255, verbose_name='Contact_Person_Relationship')),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Department_ID', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Department_ID')),
                ('Department_Manger_ID', models.DecimalField(decimal_places=0, max_digits=18, verbose_name='Department_Manger_ID')),
                ('Department_Name', models.CharField(max_length=255, verbose_name='Department_Name')),
                ('Department_Type', models.IntegerField(verbose_name='Department_Type')),
                ('Bank_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.Bank')),
            ],
            options={
                'db_table': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('Loan_ID', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Loan_ID')),
                ('Loan_Total', models.FloatField(verbose_name='Loan_Total')),
                ('Loan_Status', models.CharField(default='0', max_length=1, verbose_name='Loan_Status')),
                ('Bank_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.Bank')),
            ],
            options={
                'db_table': 'Loan',
            },
        ),
        migrations.CreateModel(
            name='SavingAccount',
            fields=[
                ('SAccount_ID', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='SAccount_ID')),
                ('SAccount_Balance', models.FloatField(default=0.0, verbose_name='SAccount_Balance')),
                ('SAccount_Open_Date', models.DateTimeField(verbose_name='SAccount_Open_Date')),
                ('SAccount_Last_Access_Date', models.DateTimeField(auto_now=True, verbose_name='SAccount_Last_Access_Date')),
                ('SAccount_Interest_Rate', models.FloatField(verbose_name='SAccount_Interest_Rate')),
                ('SAccount_Currency_Type', models.CharField(max_length=255, verbose_name='SAccount_Currency_Type')),
                ('SAccount_Open_Bank_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.Bank')),
            ],
            options={
                'db_table': 'SavingAccount',
            },
        ),
        migrations.CreateModel(
            name='LoanRelease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loan_Release_ID', models.CharField(max_length=255, verbose_name='Loan_Release_ID')),
                ('Loan_Release_Date', models.DateTimeField(verbose_name='Loan_Release_Date')),
                ('Loan_Release_Amount', models.FloatField(verbose_name='Loan_Release_Amount')),
                ('Loan_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.Loan')),
            ],
            options={
                'db_table': 'LoanRelease',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employee_ID', models.CharField(max_length=18, primary_key=True, serialize=False, verbose_name='Employee_ID')),
                ('Employee_Name', models.CharField(max_length=255, verbose_name='Employee_Name')),
                ('Employee_Phone_Number', models.DecimalField(decimal_places=0, max_digits=11, verbose_name='Employee_Phone_Number')),
                ('Employee_Address', models.CharField(max_length=255, verbose_name='Employee_Address')),
                ('Employee_Hire_Date', models.DateTimeField(verbose_name='Employee_Hire_Date')),
                ('Employee_Type', models.IntegerField(verbose_name='Employee_Type')),
                ('Bank_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.Bank')),
                ('Department_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.Department')),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='CustomerToSA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SAccount_Last_Access_Date', models.DateTimeField(auto_now=True, verbose_name='SAccount_Last_Access_Date')),
                ('Customer_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.Customer')),
                ('SAccount_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.SavingAccount')),
                ('SAccount_Open_Bank_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.Bank')),
            ],
            options={
                'db_table': 'CustomerToSA',
            },
        ),
        migrations.CreateModel(
            name='CustomerToLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.Customer')),
                ('Loan_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.Loan')),
            ],
            options={
                'db_table': 'CustomerToLoan',
            },
        ),
        migrations.CreateModel(
            name='CustomerToCA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CAccount_Last_Access_Date', models.DateTimeField(auto_now=True, verbose_name='CAccount_Last_Access_Date')),
                ('CAccount_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.CheckAccount')),
                ('CAccount_Open_Bank_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.Bank')),
                ('Customer_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.Customer')),
            ],
            options={
                'db_table': 'CustomerToCA',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='Employee_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankManagement.Employee'),
        ),
        migrations.AddConstraint(
            model_name='loanrelease',
            constraint=models.UniqueConstraint(fields=('Loan_ID', 'Loan_Release_ID'), name='LoanRelease Fake Primary Key'),
        ),
        migrations.AddConstraint(
            model_name='customertosa',
            constraint=models.UniqueConstraint(fields=('Customer_ID', 'SAccount_Open_Bank_Name'), name='One customer is only allowed to open one SA in one bank'),
        ),
        migrations.AddConstraint(
            model_name='customertosa',
            constraint=models.UniqueConstraint(fields=('SAccount_ID', 'Customer_ID'), name='CustomerToSA Fake Primary Key'),
        ),
        migrations.AddConstraint(
            model_name='customertoloan',
            constraint=models.UniqueConstraint(fields=('Loan_ID', 'Customer_ID'), name='Primary key'),
        ),
        migrations.AddConstraint(
            model_name='customertoca',
            constraint=models.UniqueConstraint(fields=('Customer_ID', 'CAccount_Open_Bank_Name'), name='One customer is only allowed to open one CA in one bank'),
        ),
        migrations.AddConstraint(
            model_name='customertoca',
            constraint=models.UniqueConstraint(fields=('CAccount_ID', 'Customer_ID'), name='CustomerToCA Fake Primary Key'),
        ),
    ]
