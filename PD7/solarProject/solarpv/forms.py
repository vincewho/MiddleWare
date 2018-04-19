# solarProject/forms.py
from django import forms
from backend.models import User, Manufacturer, Product, TestLab

# class registerForm(forms.Form):
# fname = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': '', 'placeholder': 'First Name'}))
# lname = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': '', 'placeholder': 'Last Name'}))
# mname =
# uname =
# passwrd =
# confpasswrd =
#


class registerForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = ('username', 'fname', 'lname', 'mname', 'address', 'officenum', 'cellnum', 'email',)
        fields = '__all__'
        labels = {
            'fname': 'First Name',
            'lname': 'Last name',
            'mname': 'Middle name',
            'officenum': 'Office Number',
            'cellnum': 'Cell Number'}


class registerModForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class registerTestLabForm(forms.ModelForm):
    class Meta:
        model = TestLab
        fields = '__all__'


class registerProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
