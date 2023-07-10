from django import forms
from .models import Customer

class ProfileForm(forms.Form):
    avatar = forms.FileField()

class CustomerForm(forms.Form):
    name = forms.CharField(label="Customer name", max_length=100, error_messages={
        "required" : "this field is required!",
        "max_length": "name is too long"
    })

    class Meta:
        model = Customer
        fields = '__all__'
