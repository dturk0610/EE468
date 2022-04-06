
def is_student(user):
    return user.groups.filter(name='student').exists()

def is_admin(user):
    return user.groups.filter(name='admin').exists()

def is_prof(user):
    return user.groups.filter(name='prof').exists()
