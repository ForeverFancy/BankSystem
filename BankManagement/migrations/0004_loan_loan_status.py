# Generated by Django 3.0.7 on 2020-06-26 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankManagement', '0003_remove_loan_loan_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='Loan_Status',
            field=models.CharField(default='0', max_length=1, verbose_name='Loan_Status'),
        ),
    ]