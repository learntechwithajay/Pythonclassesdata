# using member vaiables and methods of one class inside the another class:
# 1. Has - A Relationship (By-composition)
# 2. Is-A Relationship (By-Inheritance)
#
# Has - A Relationship:
#  By using Class Name or by creating object we can access members of one class inside  another class is nothing but By composition (Has-A Relationship)
# class Test:
#
#     num1 = 67
#     def __init__(self):
#         self.num2 = 40
#         print("Test class variable:", self.num2)
#
#     def method_1(self):
#         print("first class method execute..")
#
# class CTest:
#
#     def __init__(self):
#         self.t1 = Test()
#
#     def second_method(self):
#         print("Test class vairable Num1 value:",self.t1.num1)
#         print("Test Class variable Num2 value:", self.t1.num2)
#         self.t1.method_1()
#
#
# ct = CTest()
# ct.second_method()
#
# ___________________________
# parent class -->  stock ---> date, stockId, quantity
# child class --> product --> method , instance method , product
# class PClass:
#     num1 = 60
#     def __init__(self):
#         self.num2 = 90
#
#     def m1(self):
#         print("Parent method m1 calling ...")
#
# class  CHClass:
#     num3 = 100
#
#     def __init__(self):
#         self.num4 = 800
#
#     def m2(self):
#         print("Child class m2 method calling...")
#
#     def m3(self):
#         pobject = PClass()
#         print("Parent class variable num1 value is:",  pobject.num1)
#         print("Parent class variable num2 value is:", pobject.num2)
#         pobject.m1()
#
#         print("Child class variable num3 value:", CHClass.num3)
#         print("Child class Constructure instance variable value:", self.num4)
#         self.m2()
#         print("Child class m3 method calling... ")
#
# c1 = CHClass()
# c1.m3()

# By Inheritance (IS-A Relationship):
# What ever variables, methods and constructors available in the parent class by default
# available to the child classes and we are not required to rewrite. Hence the main
# advantage of inheritance is Code Reusability and we can extend existing functionality
# with some more extra functionality.

# Syntax: class childname(parentclassname):
#
# class Test:
#     a = 50
#
#     def __init__(self):
#         self.b = 800
#
#     def m1(self):
#         self.c = 30
#         print("Parent class instance method calling")
#
#     @classmethod
#     def m2(cls):
#         print("Parent class class method calling")
#
#     @staticmethod
#     def m3():
#         print("Parent class static method calling..")
#
# class CClass(Test):
#     c = 600
#
# c1 = CClass()
# print("Parent class variable a value:", c1.a)
# print("Parent class constructure variable value:", c1.b)
# c1.m1()
# c1.m2()
# c1.m3()
# print("Child class variable value:", c1.c)
# Composition:
# Without existing container object if there is no chance of existing contained object then
# the container and contained objects are strongly associated and that strong association is
# nothing but Composition.
# Eg: University contains several Departments and without existing university object there
# is no chance of existing Department object. Hence University and Department objects are
# strongly associated and this strong association is nothing but Composition.
#
# Aggregation:
# Without existing container object if there is a chance of existing contained object then the
# container and contained objects are weakly associated and that weak association is
# nothing but Aggregation.
# Eg: Department contains several Professors. Without existing Department still there may
# be a chance of existing Professor. Hence Department and Professor Objects are weakly
# associated, which is nothing but Aggregation.







































