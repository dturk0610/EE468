from http.client import HTTPResponse
import re
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Department, Instructor
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Max, Min, Avg


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def allDepartment(request):
    dept_info = ""
    for dept in Department.objects.all():
        dept_info += f'<p>{dept}</p>'
    html = "<html><h1>Test page.</h1><h2>All Department info:</h2>" + dept_info + "</html>"
    
    return HttpResponse(html)

def F1(request):
    if (request.method=='GET'):
        html = ""
        orderByType = request.GET.get('orderByType', 'name') #'name', 'dept_name', 'salary' should only be
        orderByType = orderByType.split(",")
        orderByType = list(set(orderByType) & set(['name', 'dept_name', 'salary']))
        for i in Instructor.objects.all().order_by(*orderByType):
            html += f'<p>{i}</p>'
        return HttpResponse(html)
    else:
        return HTTPResponse("Please use GET");


def F2(requst):
    html = ""
    for dept in Department.objects.all():
        res = list(Instructor.objects.filter( dept_name = dept.dept_name ).aggregate(Min('salary'), Max('salary'), Avg('salary')).values())
        html += f'<p>{dept.dept_name} Min:{res[0]} Max:{res[1]} Avg:{res[2]}</p>'
    return HttpResponse(html)

def controlPanel(request):
    return render(request, 'controlPanel.html')

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


def is_student(user):
    return user.groups.filter(name='Student').exists()

@login_required
@user_passes_test(is_student)
def onlyStudent(request):
    return HttpResponse("You are a student")
