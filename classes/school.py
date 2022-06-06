from doctest import script_from_examples
from opcode import stack_effect
from unicodedata import name
from student import Student
from staff import Staff

class School:
    def __init__(self,name) -> None:
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()
    
    
# print(School.__dict__)