from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):

    return render(request , 'home.html' , {'name':'Prakash'})

def add(request):

    value1 = request.GET['num1']
    value2 = request.GET['num2']
    res = value1 + value2

    return render(request , 'result.html' )

