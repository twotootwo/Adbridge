from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'logg/index.html')  
def hello(request):
    return render(request, 'logg/hello.html')