# Generated by Django 3.0.7 on 2020-06-26 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BankManagement', '0002_auto_20200626_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='Loan_Status',
        ),
    ]
