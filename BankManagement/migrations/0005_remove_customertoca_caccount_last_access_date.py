# Generated by Django 3.0.7 on 2020-06-27 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BankManagement', '0004_loan_loan_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customertoca',
            name='CAccount_Last_Access_Date',
        ),
    ]