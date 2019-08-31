from django.shortcuts import render
from .models import Student,Teacher
from math import ceil

def index(request):

    std=Student.objects.all()
    tch=Teacher.objects.all()
    n2=len(tch)
    nslides2 = n2 // 4 + ceil((n2 / 4) - (n2 // 4))
    n=len(std)
    nslides=n//4+ceil((n/4)-(n//4))
    allstd=[[std,range(1,len(std)),nslides],
            [std, range(1, len(std)), nslides],[tch, range(1, len(tch)), nslides2]]
    params={'allstd':allstd}
    return render(request,'index.html',params)
def about(request):
    return render(request,'about.html')
def tracker(request):
    return render(request,'index.html',{'name':'shivam'})
def contact(request):
    return render(request,'contact.html')



