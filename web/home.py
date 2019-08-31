from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("it is home page ")
def index(request):
    return render(request,'index.html')

