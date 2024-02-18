from django.shortcuts import render
from .models import Product,Customer,Orders


# Create your views here.


def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    total_orders = Orders.objects.filter(customer=customer).count()
    items = Product.objects.filter(customer=customer).order_by('-date') # get the last
    context = {'customer':customer,
               'total_orders':total_orders
               
               
               }

    return render (request,'customer.html',context)


def dashboard(request):
    customers = Customer.objects.all()
    orders =Orders.objects.all()
    total_customers = customers.count() # to get the no. of customer objects
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending= orders.filter(status='Pending').count()


    context = {'customers':customers,
               'orders':orders,
               'total_customers':total_customers,
               'total_orders':total_orders,
               'delivered':delivered,
               'pending':pending
               }
               
    return render(request,'dashboard.html',context)

def products(request):
    products =Product.objects.all()
    context = {'products':products}
    return render(request,'products.html',context)