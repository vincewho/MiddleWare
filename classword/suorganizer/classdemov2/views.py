from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import comment

# Create your views here.


def index(request):
    return render(request, 'classdemov2/index.html')


def contact(request):

    if request.method('POST'):
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return redirect('index')
            form = CommentForm()
            context = {'form': form}

    return render(request, 'classdemov2/contactus.html', context)
