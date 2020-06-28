from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'BankFrontend/index.html')


def dist_index(request):
    return render(request, 'BankFrontend/dist/index.html')
