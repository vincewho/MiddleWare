from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'solarpv/solarPV_Home.html')

def regU(request):
  return render(request, 'solarpv/solarPV_Register.html')
  
def regM(request):
  return render(request, 'solarpv/solarPV_RegisterModule.html')