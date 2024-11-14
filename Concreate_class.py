#
# Concrete class: In Python, a concrete class is a class that provides implementations for all of its methods and can be
# instantiated to create objects. Unlike abstract classes, which serve as templates and usually have some methods
# defined without implementations, concrete classes are complete and can be used directly.
# Concreate class vs Abstract Class vs Inteface:
# 1) If we dont know anything about implementation just we have requirement specification then we should go for interface.
# 2) If we are talking about implementation but not completely then we should go for abstract class. (partially implemented class).
# 3) If we are talking about implementation completely and ready to provide service then we should go for concrete class.

# from abc import *
# class Test(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#
#     @abstractmethod
#     def m2(self):
#         pass
#     @abstractmethod
#     def m3(self):
#         pass
#
# class Test2(Test):
#     def m1(self):
#         print("m1 method implemented in Child class of Test2")
#     def m2(self):
#         print("m2 method implemented in child class of Test2")
#
# class Test3(Test2):
#     def m3(self):
#         print("m3 method implemented in child class of Test3.")
#
# t3 = Test3()
# t3.m1()
# t3.m2()
# t3.m3()
# m1 method implemented in Child class of Test2
# m2 method implemented in child class of Test2
# m3 method implemented in child class of Test3.

# Public, protected , private attributes:
#
# Public attribute:  By default in python every attribute is a public. We can access anywhere with in the class outside side class also
# such kind of attribute is called a public attribute.
#
# name = "ajay"
# class Test:
#     print("name is:", name)
#
# Protected attributes: Protected attributes can be accessed within the class anywhere but from outside of the
# class only in child classes. We can specify an attribute as protected by prefexing with _ symbol
#
#
# class Test1:
#     _fullname = "Ajay kumar"
#     print("full name :", _fullname)
#     def m1(self):
#         print("fullname:", Test1._fullname)
# class Test2(Test1):
#     print("fullname:",Test2._fullname)
#
#
# Private:  private attributes can be accessed only within the class.i.e from outside of the class we
# cannot access. We can declare a variable as private explicitly by prefexing with 2 underscore symbols.

# class Test:
#     a = 40  # Public variable or attribute
#     _b = 50  # protected variable or attribute
#     __c = 60  # private variable or attribute
#
#     def m1(self):
#         print("Public attribute value:", Test.a)
#         print("Protected attribute value:", Test._b)
#         print("Private attribute value:", Test.__c)
#
# tobj = Test()
# tobj.m1()
# print("Public attribute calling outside of the class:", Test.a)
# print("Protected attribute calling outside of the class:", Test._b)
# print("Private attribute calling outside to the class:", Test.__c)
# Public attribute value: 40
# Protected attribute value: 50
# Private attribute value: 60
# Public attribute calling outside of the class: 40
# Protected attribute calling outside of the class: 50
# Traceback (most recent call last):
#   File "C:\Users\DCS\Desktop\git_repo_python_class\Pythonclassesdata\Concreate_class.py", line 80, in <module>
#     print("Private attribute calling outside to the class:", Test.__c)
# AttributeError: type object 'Test' has no attribute '__c'


# class Test:
#
#     def __init__(self):
#         self.__num = 40
#
# tobj = Test()
# print("Num private attribute value:", tobj._Test__num)

# Num private attribute value: 40
# __str__() method:
#  Whenever we are printing any object reference internally __str__() method will be
# called which is returns string in the following format
# <__main__.classname object at 0x022144B0>

# class Test:
#     def __init__(self):
#         self.num = 50
#         print("Num value:", self.num)
#
# tobj = Test()
# print(tobj)
# Num value: 50
# <__main__.Test object at 0x0000025F3376B400>


# class Student:
#     def __init__(self, name, sid):
#         self.name = name
#         self.sid = sid
#
#     def __str__(self):
#         return 'This is string method overriding to show student name is:{} \n student id is: {}'.format(self.name, self.sid)
#
# s1 = Student("Ajay", 1001)
# s2 = Student("Himajesh", 1002)
# print(s1)
# print(s2)

# <__main__.Student object at 0x00000137E3C3B400>
# <__main__.Student object at 0x00000137E3C868E0>
#
# This is string method overriding to show student name is:Ajay
#  student id is: 1001
# This is string method overriding to show student name is:Himajesh
#  student id is: 1002
#
# banking application:
#
# parent class Account: --> postional arguaments --> balance , cname, account id, min_balance, withdraw, deposite, printstatement
#
# Child class--> Saving account, current account, ---> parent class consume--> saving operation perform


















