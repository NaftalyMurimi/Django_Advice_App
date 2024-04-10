# from  django import forms
# from .models import Subscribers

# class mySubscribers(forms.ModelForm):
#     class Meta:
#         model = Subscribers
#         fields = ["Username", "Email", "Password"]


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django import forms
from django.forms.widgets import PasswordInput,TextInput

#Create a user
class Subscribers(UserCreationForm): 
    class Meta: 
        model=User 
        fields=['username','email','password1','password2',]


#Create authenitcation for to login
class loginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget= PasswordInput())