# Garbage Collector:

# # passing member varibles one class to another class:
# class Employee:
#
#     def __init__(self, name, eno, esal):
#         self.ename = name
#         self.eno = eno
#         self.esal = esal
#
#     def display(self):
#         print("Employee Number:", self.eno)
#         print("Employee Name:", self.ename)
#         print("Employee Salary:", self.esal)
#
# class Test:
#     def modify_sal(emp):
#         emp.esal = emp.esal + 5000
#         emp.display()
#
#
# e = Employee("Ajay", 1001, 25000)
# Test.modify_sal(e)

# inner class: one class location inside create another class is called inner class
# class mainclass:
#     def __init__(self):
#         pass
#
#     def m1(self):
#         pass
#
#     class inner_class:
#
#         def __init__(self):
#             pass
#
#         def m2(self):
#             pass

# class College:
#
#     def __init__(self):
#         print("Main class...")
#
#     class Employee:
#
#         def __init__(self):
#             self.ename = "ajay"
#             self.eno = 1001
#             self.esal = 20000
#
#         def display_employee(self):
#             print("Employee name:", self.ename)
#             print("Employee Number:", self.eno)
#             print("Employee Salary:", self.esal)

# c = College()
# e = c.Employee()
# e.display_employee()

# e = College().Employee()
# e.display_employee()
# College().Employee().display_employee()
















































