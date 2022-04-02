from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Department


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def allDepartment(request):
    dept_info = ""
    for dept in Department.objects.all():
        dept_info += f'<p>{dept}</p>'
    html = "<html><h1>Test page.</h1><h2>All Department info:</h2>" + dept_info + "</html>"
    
    return HttpResponse(html)