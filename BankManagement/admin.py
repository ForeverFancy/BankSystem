from django.contrib import admin
from BankManagement.models import *

# Register your models here.
admin.site.register(Bank)
admin.site.register(CheckAccount)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(CustomerToCA)
admin.site.register(Loan)
admin.site.register(CustomerToLoan)
admin.site.register(SavingAccount)
admin.site.register(CustomerToSA)
admin.site.register(LoanRelease)
