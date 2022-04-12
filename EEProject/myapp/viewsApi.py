from django.http import HttpResponse, JsonResponse
from setuptools import find_packages
from myapp.models import Department, Instructor, Teaches, Takes
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
        counter = 0;
        for i in Instructor.objects.order_by(*orderByType):
            insts[counter] = {"name":i.name, "dept_name":i.dept_name.dept_name, "salary":i.salary}
            counter = counter + 1
        return JsonResponse(insts)
    else:
        return HttpResponse("Please use GET")

@login_required
@user_passes_test(is_admin)
def F2(request):
    d = {}
    counter = 0
    for dept in Department.objects.all():
        res = list(Instructor.objects.filter( dept_name = dept.dept_name ).aggregate(Min('salary'), Max('salary'), Avg('salary')).values())
        d[counter] = {"dept":dept.dept_name, "min": res[0], "max": res[1], "avg": res[2]}
        counter = counter + 1
    return JsonResponse(d)

#@login_required
#@user_passes_test(is_admin)
def F3(request):
    logging.basicConfig(level=logging.NOTSET)
    sem = 1
    year = 2019
    for i in Instructor.objects.all():
        count = 0
        for teaches in Teaches.objects.all().filter(semester = sem, year = year, id = i.id):
            for takes in Takes.objects.all().filter(semester = sem, year = year):
                #if str(takes.course.course_id) == str(teaches.course.course_id):

                logging.info(serializers.serialize('json', takes))
            count += 1
            logging.info(teaches)
        logging.info(count)
    return HttpResponse(' ')
