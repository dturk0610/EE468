from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    # front facing
    path('', views.controlPanelRedirect, name='controlPanelRedirect'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('controlPanel', views.controlPanel, name='controlPanel'),
    path('login/', views.loginRedirect, name='loginRedirect'),
    path('admin/', admin.site.urls),
    
    # api paths
    path('api/F1', views.F1, name='F1'),
    path('api/F2', views.F2, name='F2'),
    path('api/F3', views.F3, name='F3'),
    path('api/apiTest', views.apiTest, name='apiTest'),

    # test paths
    path('allDepartment', views.allDepartment, name='allDepartment'),
    path('apiStudent', views.apiStudent, name='apiStudent'),
    path('testTemplate', views.testTemplate, name='testTemplate'),
    path('test', views.test, name='test'),
    path('apiTestPage', views.apiTestPage, name='apiTestPage'),
    path('onlyStudent', views.onlyStudent, name='onlyStudent'),
]