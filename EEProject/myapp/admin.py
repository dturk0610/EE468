from django.contrib import admin
from myapp.models import Department, Instructor, Student

# Register your models here.
admin.site.register(Department)
admin.site.register(Instructor)
admin.site.register(Student)
