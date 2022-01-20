"""
Program: overriding.py
Author: Duroje Gwaamna
Date Last Modified: 11/21/2021

This program creates two derived classes from the base Employee class. Each derived class has its own methods to update either a salary or hourly pay.
Both classes have a display mehtod that differs depending on the derived class created
"""



class Employee:

    def __init__ (self, lname, fname):
        self.last_name = lname
        self.first_name = fname

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

class SalariedEmployee(Employee):

    def __init__(self, lname, fname, start, _salary):
        self.start_date = start
        self.salary = _salary
        super().__init__(lname, fname)

    def give_raise(self, _salary):
        self.salary = _salary

    def display(self):
        print("Employee: ", self.last_name, ",",self.first_name,'\n',"Start date: ", self.start_date,  '\n', "Salary: ${:.2f}".format(self.salary))

class HourlyEmployee(Employee):

    def __init__(self, lname, fname, start, _pay):
        self.start_date = start
        self.hourly_pay = _pay
        super().__init__(lname, fname)

    def give_raise(self, _pay):
        self.hourly_pay = _pay

    def display(self):
        print("Employee: ", self.last_name, ",",self.first_name,'\n',"Start date: ", self.start_date, '\n', "Hourly pay: ${:.2f}".format(self.hourly_pay))


# driver

employee = HourlyEmployee("Gwmana", "Duroje", "5/25/2017", 10.00)
employee.give_raise(12)
employee.display()

manager = SalariedEmployee("Gwmana", "Sarah", "5/8/2012", 40000)
manager.give_raise(45000)
manager.display()

del employee
del manager

    

        
