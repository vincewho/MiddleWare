# homedemo/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm, ContactForm, teamForm

# Create your views here.


def homedemo(request):
    # if this is a POSt request, we need to process the form data
    if request.method == 'POST':
        # create form instance & populate with data from request.
        form = ContactForm(request.POST)
        # check if valid
        if form.is_valid():
            # django does magic in here
            # redirect after it's done to some link
            return HttpResponseRedirect('/homedemo/')

    else:
        # if form is blank or doesn't work right.
        form = ContactForm()

    return render(request, 'homedemo/index.html', {'form': form})


def sport(request):

    if request.method == 'POST':
        form = teamForm(request.POST)
        form1 = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/homedemo/sport/')

    else:
        form = teamForm()
        form1 = ContactForm()

    return render(request, 'homedemo/testsport.html', {'form': form, 'form1': form1})
