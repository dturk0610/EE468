from django.http import HttpResponse, JsonResponse
from setuptools import find_packages
from myapp.models import Department, Instructor
from django.db.models import Max, Min, Avg
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core import serializers
import json
from myapp.authTools import *


#decorations reference is_[permission] from authTools.py
@login_required
@user_passes_test(is_student)
def F1(request):
    if (request.method=='GET'):
        html = ""
        orderByType = request.GET.get('orderByType', 'name') #'name', 'dept_name', 'salary' should only be
        orderByType = orderByType.split(",")
        orderByType = list(set(orderByType) & set(['name', 'dept_name', 'salary']))
        # for i in Instructor.objects.all().order_by(*orderByType):
        #     html += f'<p>{i}</p>'
        jsonString = serializers.serialize("json", Instructor.objects.all().order_by(*orderByType), fields = ["name", "dept_name", "salary"])
        return HttpResponse(jsonString, content_type="application/json")
    else:
        return HttpResponse("Please use GET")

@login_required
@user_passes_test(is_student)
def F2(request):
    html = ""
    d = {}
    for dept in Department.objects.all():
        res = list(Instructor.objects.filter( dept_name = dept.dept_name ).aggregate(Min('salary'), Max('salary'), Avg('salary')).values())
        d[dept.dept_name] = {"min": res[0], "max": res[1], "avg": res[2]}
        # html += f'<p>{dept.dept_name} Min:{res[0]} Max:{res[1]} Avg:{res[2]}</p>'
    return JsonResponse(d)
    # return HttpResponse(html)


