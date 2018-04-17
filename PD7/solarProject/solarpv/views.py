from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import registerForm, registerModForm, productForm
from backend.models import Manufacturer
# User, Manufacturer, Product

# Create your views here.


def home(request):
    return render(request, 'solarpv/solarPV_Home.html')


def regU(request):

    if request.method == 'POST':
        userForm = registerForm(request.POST)

        if userForm.is_valid():
            # allow when testing is finished
            userForm.save()
            return HttpResponseRedirect('/')

    else:
        form = registerForm()

    context = {'form': form}

    return render(request, 'solarpv/solarPV_Register.html', context)


def regM(request):

    if request.method == 'POST':
        manuForm = registerModForm(request.POST)
        proForm = productForm(request.POST)

        if all([manuForm.is_valid(), proForm.is_valid()]):
            # allow when testing is finished
            manuForm.save()
            pro = proForm.save(commit=False)
            pro.manufacturer = 'manufacturer'
            pro.save()
            return HttpResponseRedirect('/')

    else:
        proForm = productForm(prefix="proForm")
        manuForm = registerModForm(prefix="manuForm")

    context = {
        'form1': registerModForm,
        'form': productForm}

    return render(request, 'solarpv/solarPV_RegisterModule.html', context)


def testp(request):
    return render(request, 'solarpv/solarPV_TestingPage.html')


def rating(request):
    return render(request, 'solarpv/solarPV_RatingPage.html')
