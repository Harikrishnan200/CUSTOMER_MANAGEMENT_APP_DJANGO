from django.shortcuts import render,redirect
from .models import Product,Customer,Orders
from .forms import OrderForm
from django.forms import inlineformset_factory

# Create your views here.


def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    total_orders = Orders.objects.filter(customer=customer).count()
    items = Orders.objects.filter(customer=customer).order_by('-created_at') 
    context = {'customer':customer,
               'total_orders':total_orders,
               'items':items
               
               
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

def create(request):

    if request.POST:
        frm = OrderForm(request.POST)
        
        if frm.is_valid():
            frm.save()
        return redirect('/')
    else:
       
        frm = OrderForm()
    return render(request,'update_order.html',{'frm':frm}) 

def remove(request,pk):
    order = Orders.objects.get(id=pk)
    if request.POST:
        order.delete()  
        return redirect('/')
    
    context={'item':order.product}
    return render(request,"delete_warning.html",context)


def update(request,pk):
    order = Orders.objects.get(id=pk)
    if request.POST:
        frm = OrderForm(request.POST,instance=order) #here update the particular instance not created
        if frm.is_valid():
            frm.save()
        return redirect('/')
    else:
        
        frm = OrderForm(instance=order)
    return render(request,'update_order.html',{'frm':frm})


def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Orders,fields=("product","status"),extra=3)
    customer = Customer.objects.get(id=pk)
    
    if request.POST:
        formset = OrderFormSet(request.POST, instance=customer, prefix='orders') #By setting prefix='orders', you are telling Django that all the forms in this formset should have a prefix of 'orders'. This prefix will be included in the form field names when they are rendered in the HTML.
        if formset.is_valid():
            formset.save()
            return redirect('customer', str(pk)) #redirect to the detail page of that customer
    else:
        formset = OrderFormSet(instance=customer, prefix='orders')
    return render(request,'update_order.html',{'formset':formset})

