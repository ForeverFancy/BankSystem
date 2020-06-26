from django.urls import include, path
from rest_framework import routers
from BankManagement.views import *


router = routers.DefaultRouter()
router.register(r'banks', BankViewSet)
router.register(r'checkaccounts', CheckAccountViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'customers', CustomerViewSet)
# router.register(r'customertoca', CustomerToCAViewSet)
router.register(r'loans', LoanViewSet)
# router.register(r'customertoloan', CustomerToLoanViewSet)
router.register(r'savingaccounts', SavingAccountViewSet)
# router.register(r'customertosa', CustomerToSAViewSet)
router.register(r'loanreleases', LoanReleaseViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
