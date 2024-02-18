from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'index.html')

def customer(request):
    return render(request,'customer.html')

def dashboard(request):
    return render(request,'dashboard.html')

def products(request):
    return render(request,'products.html')