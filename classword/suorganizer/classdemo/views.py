from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'classdemo/index.html')
    
def contactus(request):
  return render(request, 'classdemo/contactus.html')