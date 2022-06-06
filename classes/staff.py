from person import Person
import csv

class Staff(Person):
    def __init__(self, name, age, role, school_id, password) -> None:
        super().__init__(name, age, role,school_id, password)
    

    def all_staff():
        staff_list = []
        with open('/Users/dennis/Documents/CodePlatoon/Challenges/oop-school-interface-i/oop-school-interface-i/data/staff.csv', newline='') as csvfile:
            staff_database = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in staff_database:
                staff_list.append(row)
            staff_list.pop(0)
        return staff_list