from django.forms import ModelForm
from . models import Orders
from  django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']       