from person import Person
import csv

class Staff(Person):
    def __init__(self, name, age, role, password, employee_id):
        # Person.__init__(self,name, age, role, password,employee_id)
        super().__init__(name, age, role, password)
        self.employee_id = employee_id
    

    def all_staff():
        staff_list = []
        with open('/Users/dennis/Documents/CodePlatoon/Challenges/oop-school-interface-i/oop-school-interface-i/data/staff.csv', newline='') as csvfile:
            staff_database = csv.DictReader(csvfile, skipinitialspace= True)
            for row in staff_database:
                staff_list.append(Staff(**dict(row)))
        return staff_list
