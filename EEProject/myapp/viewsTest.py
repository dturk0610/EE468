from django.http import HttpResponse, JsonResponse
from myapp.models import Department, Instructor
from django.db.models import Max, Min, Avg
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render


def apiTest(request):
    return JsonResponse({"Random Json Object": "True"})

def apiTestPage(request):
    return render(request, 'apiTest.html')