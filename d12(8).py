class Employee:
    def __init__(self, emp_id, name, dept, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (dept, salary)  
    def show_details(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Dept:", self.details[0])
        print("Salary:", self.details[1])
employees = {}
for i in range(3):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    emp = Employee(emp_id, name, dept, salary)
    employees[emp_id] = emp
for emp in employees.values():
    emp.show_details()