from django import forms

class addEmployeeForm(forms.Form):
    name = forms.CharField(label='name',max_length=200)
    email = forms.EmailField(label='email',max_length=100)
    address = forms.CharField(label='address',max_length=200)
    phone = forms.IntegerField(label='phone')