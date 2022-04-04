# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Department(models.Model):
    dept_name = models.CharField(primary_key=True, max_length=25)
    building = models.CharField(max_length=25, blank=True, null=True)
    budget = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'

    def __str__(self):
        return self.dept_name + ", " + self.building + ", " + str(self.budget) 


class Instructor(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=25, blank=True, null=True)
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instructor'

    def __str__(self):
        return self.name + ", " + self.dept_name.dept_name + ", " + str(self.salary) 

class Student(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=25, blank=True, null=True)
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    tot_cred = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
