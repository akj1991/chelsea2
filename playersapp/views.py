from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('this is players list for next match')
def index2(request):
    return render(request,'ak.html')

