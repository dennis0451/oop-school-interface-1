
from student import Student
from staff import Staff

class School:
    def __init__(self) -> None:
        self.staff = Staff.all_staff()
        self.students = Student.all_students()
    
    def list_students():
        # for i, student in enumerate(self.students):
        #     print(f"{i}, {student['name']} {student['school_id']}")


        for stud in Student.all_students():
              print(stud.__dict__)
    
School.list_students()