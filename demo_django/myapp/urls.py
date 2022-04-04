from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allDepartment', views.allDepartment, name='allDepartment'),
    path('testTemplate', views.testTemplate, name='testTemplate'),
    path('test', views.test, name='test')
]