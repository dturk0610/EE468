from http.client import HTTPResponse
import re
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp.models import Department, Instructor
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Max, Min, Avg

from myapp.authTools import *
from myapp.viewsApi import *
from myapp.viewsTest import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def allDepartment(request):
    dept_info = ""
    for dept in Department.objects.all():
        dept_info += f'<p>{dept}</p>'
    html = "<html><h1>Test page.</h1><h2>All Department info:</h2>" + dept_info + "</html>"
    
    return HttpResponse(html)

def controlPanel(request):
    return render(request, 'controlPanel/controlPanel.html')

def testTemplate(request):
    context = {"data": "ABC"}
    return render(request, 'test.html', context)

def test(request):
    if(request.method == "GET"):
        budget = request.GET.get("budget")
        dept_info = ''
        for dept in Department.objects.filter(budget__gt = budget):
            dept_info += f'<p>{dept}</p>'

        return HttpResponse(f'<html>{dept_info}</html>')
    else:
        return HttpResponse("Please use get response")



@login_required
@user_passes_test(is_student)
def onlyStudent(request):
    print(request)
    return HttpResponse("You are a student")

@login_required
@user_passes_test(is_student)
def apiStudent(request):
    return JsonResponse({"A": "hi"})

