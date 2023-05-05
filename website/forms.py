from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record
class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=200 , widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields = {'username' , 'first_name' , 'last_name' ,'email' , 'password1' , 'password2'}
        


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=200 , widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=200 , widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=200 , widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(max_length=200 , widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(max_length=200 , widget=forms.TextInput(attrs={'class':'form-control'}))
    zipcode = forms.CharField(max_length=200 , widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Record
        exclude = User ,