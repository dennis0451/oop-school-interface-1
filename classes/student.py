
from person import Person
import csv

class Student(Person):

    def __init__(self, name, age, role , school_id, password) -> None:
        super().__init__(name, age, role , school_id, password)
    
    
    def all_students():
        students_list = []
        with open('/Users/dennis/Documents/CodePlatoon/Challenges/oop-school-interface-i/oop-school-interface-i/data/students.csv', newline='') as csvfile:
            student_database = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in student_database:
                students_list.append(row)
            students_list.pop(0)
        return students_list

   
# Diana = Student('Diana', 17, 'password', 'Student', 12345)
# student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}

# Diana = Student(**student_info)

