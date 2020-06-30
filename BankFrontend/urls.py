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
    path('dist/employees.html', views.employees_index),
    path('dist/400.html', views.bad_request_index),
    path('dist/404.html', views.not_found_index),
    path('dist/500.html', views.internal_server_error_index),
    path('dist/tables.html', views.tables_index),
    path('dist/charts.html', views.charts_index),
]
