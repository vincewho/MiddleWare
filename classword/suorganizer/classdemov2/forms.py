from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(max_length=20,\
        widget=forms.TextInput(attrs={'class': '', 'placeholder': 'Name'}))

    email = forms.CharField(max_length=20,\
        widget=forms.TextInput(attrs={'class': '', 'placeholder': 'Email'}))

    Message = forms.CharField(widget=forms.Textarea(attrs={'class': '', 'placeholder': 'Comment'}))
