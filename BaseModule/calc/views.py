from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello World")
    return render(request,"home.html",{'name':'Add'})

def add(request):
    # Get
    # val1 = int(request.GET['num1'])
    # val2 = int(request.GET['num2'])

    #POST
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    
    res = val1 + val2 
    return render(request, "result.html", {'result':res})

