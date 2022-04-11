from django.http import HttpResponse, JsonResponse
from setuptools import find_packages
from myapp.models import Department, Instructor, Teaches
from django.db.models import Max, Min, Avg
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core import serializers
import json
from myapp.authTools import *
import logging


#decorations reference is_[permission] from authTools.py
@login_required
@user_passes_test(is_admin)
def F1(request):
    logging.basicConfig(level=logging.NOTSET)
    if (request.method=='GET'):
        html = ""
        orderByType = request.GET.get('orderByType', 'name') #'name', 'dept_name', 'salary' should only be
        orderByType = orderByType.split(",")
        orderByType = list(set(orderByType) & set(['name', 'dept_name', 'salary']))
        insts = {}
        logging.info( Instructor.objects.order_by(*orderByType) )
        count = 0;
        for i in Instructor.objects.order_by(*orderByType):
            insts[count] = { "name":i.name, "dept_name":i.dept_name.dept_name, "salary":i.salary }
            count = count + 1
        return JsonResponse(insts)
    else:
        return HttpResponse("Please use GET")

@login_required
@user_passes_test(is_admin)
def F2(request):
    d = {}
    count = 0
    for dept in Department.objects.all():
        res = list(Instructor.objects.filter( dept_name = dept.dept_name ).aggregate(Min('salary'), Max('salary'), Avg('salary')).values())
        d[count] = { "dept":dept.dept_name, "min": res[0], "max": res[1], "avg": res[2]}
        count = count + 1
    return JsonResponse(d)

def F3(request):
    sem = 1
    year = 2019
    for i in Instructor.object.all():
        for teaches in Teaches.objects.all().filter( ID = i.ID, teach_sem = sem, teach_year = year ):
            print(teaches)
