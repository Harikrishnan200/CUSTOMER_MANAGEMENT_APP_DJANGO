from django.db import models

# Create your models here.
class  Customer(models.Model):
    name = models.CharField(max_length=50,null=True)
    phone= models.CharField(max_length=10,null=True)
    email = models.CharField(max_length=50,null = True)
    created_at = models.DateField(auto_now_add=True,null=True)

    def __str__(self) -> str:
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50,null=True)

    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    CATEGORY = ( ('Indoor','Indoor'),
                ('Out Door', 'Out Door'),
                )
    name = models.CharField(max_length=50,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=50,null=True,choices=CATEGORY)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True,null=True)
    tag = models.ManyToManyField(Tag)   #for multiple tags to one order

    def __str__(self) -> str:
        return self.name   



class Orders(models.Model):
    STATUS = (('Pending',"Pending"),
              ("Out for Delivery","Out For Delivery")
              ,("Delivered", "Delivered"))
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True, blank=True,related_name='customer_profile')
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True, blank=True,related_name='products') 
    created_at = models.DateField(auto_now_add=True,null=True)    
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    def __str__(self) -> str:
        return self.customer.name