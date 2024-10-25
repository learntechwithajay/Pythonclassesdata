# Static Variable:If the value of a variable is not varied from object to object, such type of variables we
# have to declare with in the class directly but outside of methods. Such types of variables are called Static variables.
#
# we should use static variable declaration inside the method with using the class name
# For total class only one copy of static variable will be created and shared by all objects of that class.
# We can access static variables either by class name or by object reference
# 1. In general we can declare within the class directly but from out side of any method

# class Test():
#     x = 20  # static variable
#
#     def __init__(self):
#         self.y = 30  # instance variable
#
# t1 = Test()
# t2 = Test()
# print(t1.x, t1.y)
# print(t2.x, t2.y)
# # t1.x = 100
# Test.x = 100
# print(t1.x, t1.y)   # 100, 30
# print(t2.x, t2.y)   # 100 , 30

# 2. inside the constructure using the class name :
# 3. inside the instance method by using the class name:
# 4. inside the classmethod by using the class name or cls reference varible
# 5. inside the static method by using the class name

# class Test:
#     a = 30  # directly declare inside the class
#
#     def __init__(self):   # inside the constructure by using class name
#         Test.b = 50
#
#
#     def display(self):   # inside the instance method by using class name
#         Test.c = 70
#
#     @classmethod       # inside the classmethod by using class name or cls variable
#     def m1(cls):
#         Test.d = 80
#         cls.num1 = 90
#
#     @staticmethod    # inside the staticmethod by using class name
#     def m2():
#         Test.num2 = 100

# class Test:
#
#     num = 100
#     lname = "Ajay"
#     fname = "salindra"
#     fnum = 34.5
#     fnum1 = 67.9
#     stac_emp = "Himajesh"
#     def __init__(self):  # accessing the static variable inside the constructure by using classname or self
#         print(Test.num)
#         print(self.num)
#
#     def display(self):  # instance method
#         print(Test.fname)
#         print(self.lname)
#
#     @classmethod
#     def cls_m1(cls):
#         print(cls.fnum)
#         print(Test.fnum1)
#
#     @staticmethod
#     def stac_m2():
#         print(Test.stac_emp)
#
#
# t = Test()
# t.display()
# t.cls_m1()
# t.stac_m2()























