
# from school import School
from person import Person
import csv

class Student(Person):
    
    def __init__(self, name, age, role , password, school_id):
        # Person.__init__(self,name, age, role, password,student_id)
        super().__init__(name, age, role, password)
        self.school_id = school_id
    
    def all_students():
        students_list = []
        with open('/Users/dennis/Documents/CodePlatoon/Challenges/oop-school-interface-i/oop-school-interface-i/data/students.csv', newline='') as csvfile:
            student_database = csv.DictReader(csvfile, skipinitialspace= True)
            for row in student_database:
                students_list.append(Student(**dict(row)))
        return students_list

    def __str__(self):
        return (f"{self.name.upper()}\n----------------\nage: {self.age}\nid: {self.school_id}")
       


# Diana = Student('Diana', 17, 'password', 'Student', 12345)
# student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}

# Diana = Student(**student_info)
# Student.all_students()
