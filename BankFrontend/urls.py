from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('dist/index.html', views.dist_index),
    path('dist/banks.html', views.banks_index),
    path('dist/checkaccounts.html', views.checkaccounts_index),
    path('dist/customers.html', views.customers_index),
    path('dist/loanreleases.html', views.loanreleases_index),
    path('dist/loans.html', views.loans_index),
    path('dist/savingaccounts.html', views.savingaccounts_index),
    path('dist/departments.html', views.departments_index),
    path('dist/employees.html', views.employees_index)
]
