#from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
     #return HttpResponse("HelloWorld!  I am Varsha")
     return render(request,'home.html')

def  about(request):
      #return HttpResponse("MY ABOUTPAGE")
      return render(request,'about.html')