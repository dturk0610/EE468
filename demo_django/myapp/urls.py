from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('controlPanel', views.controlPanel, name='controlPanel'),

    # test paths
    path('allDepartment', views.allDepartment, name='allDepartment'),
    path('F1', views.F1, name='F1'),
    path('testTemplate', views.testTemplate, name='testTemplate'),
    path('test', views.test, name='test'),
    path('onlyStudent', views.onlyStudent, name='onlyStudent'),
]