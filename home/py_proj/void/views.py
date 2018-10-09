from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'void/void.html')

def ind_main(request):
    return render(request, 'void/main_v.html')

def form(requests):
    return render(request, 'void/form.html')
