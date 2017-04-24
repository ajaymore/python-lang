__author__ = 'Mystique'


class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    @staticmethod
    def display_count():
        print("Total Employee %d" % Employee.empCount)

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


emp = Employee("Ajay", 10000)
emp.age = 10
emp.display_count()
emp.display_employee()
print(hasattr(emp, 'age'))
print(getattr(emp, 'age'))
setattr(emp, 'location', 'pune')
print(getattr(emp, 'location'))
delattr(emp, 'location')

from lang.F07_classes.OutsideClass import OutSideClass


class Manager(Employee, OutSideClass):
    __designation = 'Manager'

    def __init__(self, employees_reporting):
        self.employees_reporting = employees_reporting

    def reporting_me(self):
        print('I am', self.__designation, end='. ')
        print(self.employees_reporting, 'People report me')


manager = Manager(50)
manager.print_outside("Apples")
manager.reporting_me()