from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import registerForm, registerModForm, registerTestLabForm, registerProductForm
from backend.models import Manufacturer
# User, Manufacturer, Product

# Create your views here.


def home(request):
    return render(request, 'solarpv/solarPV_Home.html')


def reg(request):

    if request.method == 'POST':
        userForm = registerForm(request.POST)

        if userForm.is_valid():
            # allow when testing is finished
            userForm.save()
            return redirect('home')

    else:
        userForm = registerForm()

    context = {'form': userForm}

    return render(request, 'solarpv/solarPV_Register.html', context)


def regM(request):
    if request.method == 'POST':
        manuForm = registerModForm(request.POST)

        if manuForm.is_valid():
            # allow when testing is finished
            manuForm.save()
            return redirect('home')

    else:
        manuForm = registerModForm()

    context = {'form': manuForm}
    return render(request, 'solarpv/solarPV_RegisterModule.html', context)


def regTL(request):
    if request.method == 'POST':
        testForm = registerTestLabForm(request.POST)

        if testForm.is_valid():
            testForm.save()
            return redirect('home')

    else:
        testForm = registerTestLabForm()

    context = {'form': testForm}
    return render(request, 'solarpv/solarPV_RegisterModule.html', context)


def regPro(request):
    if request.method == 'POST':
        productForm = registerProductForm(request.POST)

        if productForm.is_valid():
            # allow when testing is finished
            productForm.save()
            return redirect('home')

    else:
        productForm = registerProductForm()

    context = {'form': productForm}
    return render(request, 'solarpv/solarPV_RegisterProduct.html', context)


def rating(request):
    return render(request, 'solarpv/solarPV_RatingPage.html')


def testp(request):
    return render(request, 'solarpv/solarPV_TestingPage.html')
