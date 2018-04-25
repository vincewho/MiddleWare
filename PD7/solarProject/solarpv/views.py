import sys, csv
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import *
from backend.models import Manufacturer
# User, Manufacturer, Product

# Create your views here.


def home(request):
	return render(request, 'solarpv/solarPV_Home.html')


def reg(request):

	if request.method == 'POST':
		userForm = registerForm(request.POST)

		if userForm.is_valid():
			userForm.clean_username()
			userForm.clean_fname()
			userForm.clean_lname()
			userForm.clean_mname()
			userForm.clean_address()
			userForm.clean_officenum()
			userForm.clean_cellnum()
			userForm.clean_email()

			userForm.save()
			return redirect('home')

	else:
		userForm = registerForm()

	context = {'form': userForm}

	return render(request, 'solarpv/solarPV_Register.html', context)


def regC(request):
	if request.method == 'POST':
		manuForm = registerModForm(request.POST)

		if manuForm.is_valid():
			# allow when testing is finished
			manuForm.clean_name()
			manuForm.clean_address()
			manuForm.clean_country()

			manuForm.save()
			return redirect('home')

	else:
		manuForm = registerModForm()

	context = {'form': manuForm}
	return render(request, 'solarpv/solarPV_RegisterCompany.html', context)


def regTL(request):
	if request.method == 'POST':
		testForm = registerTestLabForm(request.POST)

		if testForm.is_valid():
			testForm.clean_name()
			testForm.clean_address()
			testForm.clean_country()

			testForm.save()
			return redirect('home')

	else:
		testForm = registerTestLabForm()

	context = {'form': testForm}
	return render(request, 'solarpv/solarPV_RegisterCompany.html', context)


def regPro(request):
	if request.method == 'POST':
		productForm = registerProductForm(request.POST)

		if productForm.is_valid():
			# allow when testing is finished
			productForm.save()
			return redirect('home')

	else:
		productForm = registerProductForm()

	context = {'form': productFrorm}
	return render(request, 'solarpv/solarPV_RegisterProduct.html', context)


def pvModule(request):
	return render(request, 'solarpv/solarPV_PvModule.html')


def testp(request):
	if request.method == 'POST':
		form = uploadForm(request.POST, request.FILES)

		if form.is_valid():
			file = fileUpload(upload=request.FILES['upload'])

			# file is saved
			file.save()
			return redirect('home')

	else:
		form = uploadForm()

	################################
	# specifically for reading file.
	file = ''
	data = 'This is the first line'
	path = '/home/mwtester/Desktop/djangoBox/mynew_evn/solarProject/media/uploads/'
	try:
		file = open(path + 'test_results.csv')
		data = file.readlines()
		# for row in data:
		# 	print(row)
		print('In the try')
		# lines = data.split('\n')
	except:
		print('In the fail')

	context = {'form': form, 'files': file, 'lines': data}
	return render(request, 'solarpv/solarPV_TestingPage.html', context)
