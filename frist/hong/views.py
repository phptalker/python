#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    param = ["HTML", "CSS", "jQuery", "Python", "Django"]

    return render(request, 'home.html',{'param':param})
    #return HttpResponse("hello word")