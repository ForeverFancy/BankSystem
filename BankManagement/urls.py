from django.urls import include, path
from rest_framework import routers
from BankManagement.views import *


router = routers.DefaultRouter()
router.register(r'banks', BankViewSet, basename='Bank')
router.register(r'checkaccounts', CheckAccountViewSet, basename='CheckAccount')
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'customers', CustomerViewSet, basename='Customer')
router.register(r'customertoca', CustomerToCAViewSet)
router.register(r'loans', LoanViewSet, basename='Loan')
router.register(r'customertoloan', CustomerToLoanViewSet)
router.register(r'savingaccounts', SavingAccountViewSet, basename='SavingAccount')
router.register(r'customertosa', CustomerToSAViewSet)
router.register(r'loanreleases', LoanReleaseViewSet, basename='LoanRelease')
router.register(r'statisticaldata', StatisticalDataViewSet,
                basename='StatisticalData')


urlpatterns = [
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
