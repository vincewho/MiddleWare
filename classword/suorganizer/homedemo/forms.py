# homedemo/forms.py

from django import forms
from .models import NameModel


# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Name', max_length=20)
#     your_address = forms.CharField(label='Address', max_length=30)


class NameForm(forms.ModelForm):
#     your_name = forms.CharField(label='Name', max_length=20)
#     your_address = forms.CharField(label='Address')

    class Meta:
        model = NameModel
        fields = ('name', 'address',)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class teamForm(forms.Form):
    name = forms.CharField(max_length=20)
    location = forms.CharField(max_length=20)
