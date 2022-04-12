# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from email.policy import default
from django.db import models


class Advisor(models.Model):
    s = models.ForeignKey('Student', models.DO_NOTHING)
    i = models.ForeignKey('Instructor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'advisor'
        unique_together = (('s', 'i'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Classroom(models.Model):
    building = models.CharField(max_length=25)
    room_number = models.CharField(max_length=25)
    capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classroom'
        unique_together = (('building', 'room_number'),)

    def __str__(self):
        return self.building + ", " + self.room_number + ", " + str(self.capacity)


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=25)
    title = models.CharField(max_length=50, blank=True, null=True)
    dept_name = models.ForeignKey('Department', models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    credits = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'
    
    def __str__(self):
        return self.course_id + ", " + self.title + ", " + self.dept_name + ", " + str(self.credits)


class Department(models.Model):
    dept_name = models.CharField(primary_key=True, max_length=25)
    building = models.CharField(max_length=25, blank=True, null=True)
    budget = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'

    def __str__(self):
        return self.dept_name + ", " + self.building + ", " + str(self.budget) 
# Unable to inspect table 'django_admin_log'
# The error was: 'DatabaseIntrospection' object has no attribute '_parse_constraint_columns'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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

class Prereq(models.Model):
    course = models.ForeignKey(Course, models.DO_NOTHING, related_name="pre_course")
    prereq = models.ForeignKey(Course, models.DO_NOTHING, related_name='pre_prereq')

    class Meta:
        managed = False
        db_table = 'prereq'
        unique_together = (('course', 'prereq'),)


class Section(models.Model):
    course = models.ForeignKey(Course, models.DO_NOTHING, related_name="sec_course")
    sec_id = models.IntegerField()
    semester = models.CharField(max_length=25)
    year = models.TextField()  # This field type is a guess.
    building = models.ForeignKey(Classroom, models.DO_NOTHING, db_column='building', blank=True, null=True, related_name="build")
    room_number = models.ForeignKey(Classroom, models.DO_NOTHING, db_column='room_number', blank=True, null=True, related_name="room")
    time_slot = models.ForeignKey('TimeSlot', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'section'
        unique_together = (('course', 'sec_id', 'semester', 'year'),)

    def __str__(self):
        return self.course + ", " + str(self.sec_id) + ", " + self.semester + ", " + str(self.year) + ", " + self.building + ", " + self.room_number + ", " + self.time_slot


class Student(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=25, blank=True, null=True)
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_name', blank=True, null=True)
    tot_cred = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'

    def __str__(self):
        return self.name + ", " + str(self.id) + ", " + self.dept_name.dept_name + ", " + str(self.tot_cred)


class Takes(models.Model):
    studid = models.ForeignKey(Student, models.DO_NOTHING, db_column='ID', blank=True, null=True)  # Field name made lowercase.
    course = models.ForeignKey(Section, models.DO_NOTHING, blank=True, null=True, related_name="takes_course")
    sec = models.ForeignKey(Section, models.DO_NOTHING, blank=True, null=True, related_name="takes_section")
    semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='semester', blank=True, null=True, related_name="takes_semester")
    year = models.ForeignKey(Section, models.DO_NOTHING, db_column='year', blank=True, null=True, related_name="takes_year")
    grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'takes'

    def __str__(self):
        return f"{self.studid_id}, {self.course_id}, {self.sec_id}, {self.semester_id}, {self.year_id}, {self.grade}"

class Teaches(models.Model):
    instid = models.ForeignKey(Instructor, models.DO_NOTHING, db_column='ID', blank=True, null=True)  # Field name made lowercase.
    course = models.ForeignKey(Section, models.DO_NOTHING, blank=True, null=True, related_name="teach_course")
    sec = models.ForeignKey(Section, models.DO_NOTHING, blank=True, null=True, related_name="teach_sec")
    semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='semester', blank=True, null=True, related_name="teach_sem")
    year = models.ForeignKey(Section, models.DO_NOTHING, db_column='year', blank=True, null=True, related_name="teach_year")

    class Meta:
        managed = False
        db_table = 'teaches'

    def __str__(self):
        return str(self.instid) + ", " + str(self.course_id) + ", " + str(self.sec_id) + ", " + str(self.semester_id)


class TimeSlot(models.Model):
    time_slot_id = models.IntegerField(primary_key=True)
    day = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_slot'

    def __str__(self):
        return str(self.time_slot_id) + ", " + str(self.day) + ", " + str(self.start_time) + ", " + str(self.end_time)
