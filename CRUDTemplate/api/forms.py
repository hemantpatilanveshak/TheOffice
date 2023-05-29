from django import forms
from .models import Employee

# class addEmployeeForm(forms.Form):
#     name = forms.CharField(label='name',max_length=200)
#     email = forms.EmailField(label='email',max_length=100)
#     address = forms.CharField(label='address',max_length=200)
#     phone = forms.IntegerField(label='phone')

class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','email','address','phone']