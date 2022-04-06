from django.urls import path, include

from . import views

urlpatterns = [
    # front facing
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('controlPanel', views.controlPanel, name='controlPanel'),
    
    # api paths
    path('api/F1', views.F1, name='F1'),
    path('api/F2', views.F2, name='F2'),

    # test paths
    path('allDepartment', views.allDepartment, name='allDepartment'),
    path('apiStudent', views.apiStudent, name='apiStudent'),
    path('testTemplate', views.testTemplate, name='testTemplate'),
    path('test', views.test, name='test'),
    path('onlyStudent', views.onlyStudent, name='onlyStudent'),
]