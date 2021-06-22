from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def whyarehere(request):
    return render(request, 'core/whyarehere.html')

def cutestpets(request):
    return render(request, 'core/cutestpets.html')

def exitscam(request):
    return render(request, 'core/exitscam.html')

def dummylogin(request):
    return render(request, 'core/dummylogin.html') ##

def dummydata(request):
    return render(request, 'core/dummydata.html')

def succes(request):
    return render(request, 'core/succes.html')