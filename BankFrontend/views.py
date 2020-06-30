from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'BankFrontend/index.html')


def dist_index(request):
    return render(request, 'BankFrontend/dist/index.html')


def banks_index(request):
    return render(request, 'BankFrontend/dist/banks.html')


def customers_index(request):
    return render(request, 'BankFrontend/dist/customers.html')


def checkaccounts_index(request):
    return render(request, 'BankFrontend/dist/checkaccounts.html')


def savingaccounts_index(request):
    return render(request, 'BankFrontend/dist/savingaccounts.html')


def loanreleases_index(request):
    return render(request, 'BankFrontend/dist/loanreleases.html')


def loans_index(request):
    return render(request, 'BankFrontend/dist/loans.html')


def departments_index(request):
    return render(request, 'BankFrontend/dist/departments.html')


def employees_index(request):
    return render(request, 'BankFrontend/dist/employees.html')


def bad_request_index(request):
    return render(request, 'BankFrontend/dist/400.html')


def not_found_index(request):
    return render(request, 'BankFrontend/dist/404.html')


def internal_server_error_index(request):
    return render(request, 'BankFrontend/dist/500.html')


def tables_index(request):
    return render(request, 'BankFrontend/dist/tables.html')


def charts_index(request):
    return render(request, 'BankFrontend/dist/charts.html')
