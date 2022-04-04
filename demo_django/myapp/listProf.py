from models import Instructor, Department

for i in Instructor.objects.raw('SELECT * FROM myapp_Instructor ORDER BY name, dept_name, salary'):
    print(i)

for d in Instructor.objects.raw('SELECT dept_name, min(salary), max(salary), avg(salary) FROM Instructor GROUP BY dept_name'):
    print(d)