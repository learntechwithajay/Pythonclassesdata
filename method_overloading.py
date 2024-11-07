# Overloading:
#  We can use same operator or methods for different purposes.
#
# Eg 1: + operator can be used for Arithmetic addition and String concatenation
#  print(10+20)#30
#  print('ajay'+'kumar')#ajaykumar
# Eg 2: * operator can be used for multiplication and string repetition purposes.
#  print(10*20)#200
#  print('ajay'*3)
# Eg 3: We can use deposit() method to deposit cash or cheque or dd
#  deposit(cash)
#  deposit(cheque)
#  deposit(dd)
#
# There are 3 types of Overloading
#
# 1) Operator Overloading
# 2) Method Overloading
# 3) Constructor Overloading
#
# Operator Overloading:
#  We can use the same operator for multiple purposes, which is nothing but operator overloading.
#  Python supports operator overloading. but using the magic methods otherwise python not supported for operator overloading.

# class Book:
#     def __init__(self, pages):   # b1 --> pages = 100  , b2 --> pages = 200
#         self.pages = pages
#
#     def __add__(self, other):
#         return self.pages + other.pages
#
#
# b1 = Book(100)
# b2 = Book(200)
# print("Total pages of two book:", b1 + b2)

# without magic methods its show error
#    print("Total pages of two book:", b1 + b2)
# TypeError: unsupported operand type(s) for +: 'Book' and 'Book'

# Total pages of two book: 300

# object.__add__(self,other)
# object.__sub__(self,other)
# object.__mul__(self,other)
# object.__div__(self,other)
# object.__floordiv__(self,other)
# object.__mod__(self,other)
# object.__pow__(self,other)
# object.__iadd__(self,other)
# object.__isub__(self,other)
# object.__imul__(self,other)
# object.__idiv__(self,other)
# object.__ifloordiv__(self,other)

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def __mul__(self, other):
#         return self.salary * other.days
#
# class TimeSheet:
#
#     def __init__(self, name, days):
#         self.name = name
#         self.days = days
#
# e1 = Employee("ajay", 900)
# ts = TimeSheet("ajay", 25)
#
# print("Employee Month salary", e1 * ts)

# Employee Month salary 22500

# Method Overloading:
#  If 2 methods having same name but different type of arguments then those methods are said to be overloaded methods.
#  Eg: m1(int a)
#  m1(double d)
#  But in Python Method overloading is not possible.
#  If we are trying to declare multiple methods with same name and different number of arguments then Python
# will always consider only last method.

class Test:

    def m1(self):
        print("No arguments")
    def m1(self,a):
        print("Single argument")

    def m1(self, a, b):
        print("Two arguments")

t1 = Test()
# t1.m1()
#    t1.m1()
# TypeError: m1() missing 2 required positional arguments: 'a' and 'b'
# t1.m1(20)
#     t1.m1(20)
# TypeError: m1() missing 1 required positional argument: 'b'
t1.m1(20, 40)
# Two arguments









