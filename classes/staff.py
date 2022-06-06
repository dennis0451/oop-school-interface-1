from person import Person
import csv

class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role,employee_id, password)
    

    def all_staff():
        staff_list = []
        with open('/Users/dennis/Documents/CodePlatoon/Challenges/oop-school-interface-i/oop-school-interface-i/data/staff.csv', newline='') as csvfile:
            staff_database = csv.DictReader(csvfile, skipinitialspace= True)
            for row in staff_database:
                staff_list.append(Staff(**dict(row)))
        print(staff_list)
Staff.all_staff()