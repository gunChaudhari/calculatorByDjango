from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse("Hello World")
    return render(request, 'home.html',{'name':'Gunjan'})

def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    res = val1 + val2
    return render(request, 'result.html', {'result': res})

def sub(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 - val2
    return render(request, 'result.html', {'result': res})

def mul(request):


    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 * val2
    return render(request, 'result.html', {'result': res})

def div(request):


    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 / val2
    return render(request, 'result.html', {'result': res})