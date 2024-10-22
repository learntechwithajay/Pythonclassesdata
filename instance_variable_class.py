# Constructor Concept:
# Constructor is a special method in python.
# The name of the constructor should be __init__(self)
# Constructor will be executed automatically at the time of object creation.
# The main purpose of constructor is to declare and initialize instance variables.
# Per object constructor will be exeucted only once.
# Constructor can take atleast one argument(atleast self)
# Constructor is optional and if we are not providing any constructor then python will provide default constructor.
#
# def __init__():
#     instance variable ; or reference variable

# class Test:
#
#     def __init__(self):
#         self.a = 20
#         self.b = 30
#         print("constructre execute")
#
#     def display(self):
#         print("Welcome to method")
#
# t = Test()
# print(t.__dict__)
# t.display()
# t.display()
# print(t)

# {'a': 20, 'b': 30}

# 1. In python constructure name should be declare always __init__()
# 2. in python method name given for user defined
# 3. method will be exected if call that method
# 4. constructure if create an object by default its execute. how many time only once

# types of variables in python:
# 1. Instance variables: (object level variables)
# 2. static variables(): (class level variables)
# 3. local variables: (method level variables)

# 1. Instance variables: (object level variables)
#
# If the value of a variable is varied from object to object, then such type of variables are called instance variables.
# For every object a separate copy of instance variables will be created.

# class Test:
#     def __init__(self):
#         self.a = 40
#         self.b = 50
#         print("A value is: {} \n B value is: {}".format(self.a, self.b))
#
# t = Test()

# Where we can declare Instance Variables:
# 1) Inside Constructor by using self variable
# class Test:
#     def __init__(self):
#         self.a = 40
#         self.b = 50
#         print("A value is: {} \n B value is: {}".format(self.a, self.b))
#
# t = Test()

# 2) Inside Instance Method by using self variable
# class Test:
#
#     def display(self):
#         self.name = "ajay"
#         return self.name
#
# t = Test()
# print("My name is :", t.display())

# 3) Outside of the class by using object reference variable

# class Test:
#
#     def __init__(self):
#         self.a = 20
#
#     def display(self):
#         self.b = 50
#
# t = Test()   # t = { a:20, b: 50, c: 70}
# t.display()
# t.c = 70
# print(t.__dict__)

# how to access instance variables in a instance method:
class Test:

    def display(self):
        self.num1 = 50
        self.num2 = 60
        print(self.num1)
        print(self.num2)

t = Test()
t.display()
print(t.num1, t.num2)



































