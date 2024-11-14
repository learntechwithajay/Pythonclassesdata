# Constructor Overloading:
# ⚽ Constructor overloading is not possible in Python.
# ⚽ If we define multiple constructors then the last constructor will be considered

# class Test:
#     def __init__(self):
#         print("Without argument")
#     def __init__(self,a):
#         print("One argument")
#
#     def __init__(self, a, b):
#         print("Two arguments")

# t = Test()
# TypeError: __init__() missing 2 required positional arguments: 'a' and 'b'
# t = Test(20)
# TypeError: __init__() missing 2 required positional arguments: 'a' and 'b'
# t = Test(20, 30)
# Two arguments

# Constructor with default arguments:

# class Test:
#     def __init__(self, a = None, b = None, c = None):
#         print("this constructor return multiple argument..(1|2|3 arguments)")
#
# t1 = Test(20)
# t2 = Test(20,30)
# t3 = Test(20, 30, 40)
# this constructor return multiple argument..(1|2|3 arguments)
# this constructor return multiple argument..(1|2|3 arguments)
# this constructor return multiple argument..(1|2|3 arguments)

# constructor with possitional arguments variable:

# class Test:
#     def __init__(self, *args):
#         print("this constructor return multiple argument..(1|2|3 arguments)")
#
# t = Test()
# t1 = Test(20)
# t2 = Test(20,30)
# t3 = Test(20, 30, 40)
# t4 = Test(20, 30, 40, 50)
# t5 = Test(100, 200, 300, 400, 500, 600)

# this constructor return multiple argument..(1|2|3 arguments)
# this constructor return multiple argument..(1|2|3 arguments)
# this constructor return multiple argument..(1|2|3 arguments)
# this constructor return multiple argument..(1|2|3 arguments)
# this constructor return multiple argument..(1|2|3 arguments)
# this constructor return multiple argument..(1|2|3 arguments)

# class Student:
#     def __init__(self, name=None, age=None, grade=None):
#         if name and age and grade:
#             self.name = name
#             self.age = age
#             self.grade = grade
#             print(f"Student created: {self.name}, Age: {self.age}, Grade: {self.grade}")
#         elif name and age:
#             self.name = name
#             self.age = age
#             self.grade = "Unknown"  # Default grade
#             print(f"Student created: {self.name}, Age: {self.age}, Grade: {self.grade}")
#         elif name:
#             self.name = name
#             self.age = 0  # Default age
#             self.grade = "Unknown"  # Default grade
#             print(f"Student created: {self.name}, Age: {self.age}, Grade: {self.grade}")
#         else:
#             self.name = "Unknown"
#             self.age = 0
#             self.grade = "Unknown"
#             print(f"Student created with default values: {self.name}, Age: {self.age}, Grade: {self.grade}")
#
# student1 = Student("ajay", 20, "A")
# student2 = Student("sai", 18)
# student3 = Student("Himajesh")
# student4 = Student()
#
# Student created: ajay, Age: 20, Grade: A
# Student created: sai, Age: 18, Grade: Unknown
# Student created: Himajesh, Age: 0, Grade: Unknown
# Student created with default values: Unknown, Age: 0, Grade: Unknown

# Overriding:
# Method Overriding:
# ⚽ What ever members available in the parent class are bydefault available to the child class through inheritance.
# If the child class not satisfied with parent class implementation then child class is allowed to redefine
# that method in the child class based on its requirement. This concept is called overriding.
# ⚽ Overriding concept applicable for both methods and constructors.
#
# This allows the subclass to provide its specific implementation for the
#     method, while the parent class 's method can be invoked using super().


# class Test:
#     def my_method1(self):
#         print("Parent class my method1")
#
#     def my_method2(self):
#         print("Parent class my method2")
#
# class ChClass(Test):
#     def my_method1(self):
#         super().my_method1()
#         print("Child class my method1")
#
# chobj = ChClass()
# chobj.my_method1()
# Child class my method1
class Employee:
    def __init__(self, ename, base_salary):
        self.ename = ename
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

class FullTimeEmployee(Employee):
    def __init__(self, ename, base_salary, bonus):
        super().__init__(ename, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

class PartTimeEmployee(Employee):
    def __init__(self, ename, base_salary, working_hourse):
        super().__init__(ename, base_salary)
        self.working_hourse = working_hourse

    def calculate_salary(self):
        return self.base_salary * self.working_hourse


femp = FullTimeEmployee("Ajay", 5000, 1000)
print(f"Employee name:{femp.ename}.")
print(f"Salary of employee:{femp.calculate_salary()}")
pemp = PartTimeEmployee("Himajesh", 25000, 100)
print(f"Employee name:{pemp.ename}.")
print(f"Salary of employee:{pemp.calculate_salary()}")



















































