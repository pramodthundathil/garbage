from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput,PasswordInput, ModelForm, Textarea
from .models import Client, Staff
from django import forms
from django.contrib.auth.hashers import make_password




class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username','email','password1','password2']
        
        widgets = {
            "first_name":TextInput(attrs={"class":"form-control  py-3","placeholder":"First Name"}),
            "username":TextInput(attrs={"class":"form-control py-3","placeholder":"Username"}), 
            "email":TextInput(attrs={"class":"form-control py-3","placeholder":"Email Id"}),    
        }  
        
    def __init__(self, *args, **kwargs):
        super(UserAddForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control py-3', 'placeholder': 'Password'})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control  py-3', 'placeholder': 'Password confirmation'})

class UserUpdateForm(UserChangeForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput, help_text="Leave blank if not changing.")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']


    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.password = make_password(password)
        if commit:
            user.save()
        return user
    


class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ['user']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control py-3', 'placeholder': 'Name'}),
            'phone': TextInput(attrs={'class': 'form-control py-3', 'placeholder': 'Phone'}),
            'address': Textarea(attrs={'class': 'form-control py-3', 'placeholder': 'Address', 'rows': 3}),
            'location': TextInput(attrs={'class': 'form-control py-3', 'placeholder': 'Location'}),
        }


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        exclude = ['user']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control py-3', 'placeholder': 'Name'}),
            'phone': TextInput(attrs={'class': 'form-control py-3', 'placeholder': 'Phone'}),
            'address': Textarea(attrs={'class': 'form-control py-3', 'placeholder': 'Address', 'rows': 3}),
            'location': TextInput(attrs={'class': 'form-control py-3', 'placeholder': 'Location'}),
        }


