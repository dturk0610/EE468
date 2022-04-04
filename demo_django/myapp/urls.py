from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('controlPanel', views.controlPanel, name='controlPanel'),

    # test paths
    path('allDepartment', views.allDepartment, name='allDepartment'),
    path('testTemplate', views.testTemplate, name='testTemplate'),
    path('test', views.test, name='test'),
]