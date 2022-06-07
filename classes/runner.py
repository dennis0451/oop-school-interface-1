from school import School 
from staff import Staff
from student import Student



school = School('Ridgemont High') 

# school.list_students()
# school.find_student_by_id()2


# print(school.staff)
# print(school.students)
# sch
#runner.py
# print("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")
#runner.py 
mode = ''
while mode != '5':
    
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")
    if mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input('Enter student id:')
        student = school.find_student_by_id(student_id)
        print(str(student))
    else:
        pass      
print(mode)

