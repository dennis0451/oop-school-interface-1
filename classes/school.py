
from student import Student
from staff import Staff

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()
    
    def list_students(self):
        for i,student in enumerate(self.students):
            print(f"{i+1}. {student.name} {student.school_id}")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student


# print(Student.all_students())