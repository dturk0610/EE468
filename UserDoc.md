# User Document

## Initial Setup

First, create an admin account by running:

`python3 manage.py createsuperuser`

Then, run the server and login to [127.0.0.1:8000/admin](127.0.0.1:8000/admin)

Use the add buttons to add the following groups:

- `admin`
- `prof`
- `student`

Users can now be added and assigned to each group.



## Logging in
After creating the user under the required group, the user can now login using http://127.0.0.1:8000/accounts/login/ 

Here is the login page:
![login page](images/login%20page.JPG)
The user can type in the credential of the user account created and this page redirect to the respected control panel.


# The Control Panel - Admin
if you use the credentials to login for an admin account you will be redirected to the Admin section -

After logging in the admin user account, User can do following tasks:
1. Create a list of professors sorted by one of the following criteria chosen by the admin: (1) by name (2) by dept, or (3) by salary
2. Create a table of min/max/average salaries by dept
3. Create a table of professor name, dept, and total number of students taught by the professor in a given semester
   
##Now,You can see the admin section page:
![admin_section1](images/admin_section1.PNG)

The user can use the check boxes to list the professors ordered by the given attributes. Multiple inputs can be implemented too. Then clicking on the "list all professors"
button will execute the task.

The user can also click the "List all departments info " for getting table.

##Example 1: The list of professors ordered by name:

![admin_section2](images/admin_section2.PNG)

##Example 2: The list of professors ordered by all attributes:

![admin_section3](images/admin_section3.PNG)

##Example 3: The list of all departments information:

![admin_section4](images/admin_section4.PNG)

# The Control Panel - Professor

## The Control Panel - Student

if you use the credentials to login for an admin account you will be redirected to the Admin section -

After logging in the admin user account, User can do following tasks:
1. Query the list of course sections offered by dept in a given semester and year.

##Now,You can see the Student section page:
![student_section1](images/student_section1.png)

The user can use the drop down list menu to select the department,class and year to get the list of course sections.

##Example 1: When user selects CS department for CS141 of fall 2019:

![student_section2](images/student_section2.png)

##Example 2: When user selects ART department for AT200 of fall 2019:

![student_section3](images/student_section3.png)
