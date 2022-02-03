from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('this is players list for next match')

