# Abstract method:
# sometimes we don't' know about the implementation , still we can declare a method such kind of methods is called abstract methods.
#                 or
# Which method having declaration without implementation such kind of methods is called abstract methods.
# in python abstract methods declaration process using @abstractmethod decorator.
# Abstracte method implementaions are done into the child class ..
# @abstractmethod --> it is builtin method --> under the class of "ABC"(abstract base class) --> under the "abc" module

# from abc import *
# class Test:
#     @abstractmethod
#     def m1(self):
#         pass

# Abstract Class:
# Some times implementation of a class is not complete,such type of partially implementation classes are called abstract classes.
# Every abstract class in Python should be derived from "ABC" class which is present in "abc" module.
# --> abstract class contain abstract metods, and general methods are also declare.

# from abc import *
# class Test(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#
# t = Test()

#     t = Test()
# TypeError: Can't instantiate abstract class Test with abstract method m1
# If a class contains atleast one abstract method and if we are extending ABC class then instantiation is not possible

# from abc import *
#
# class Payment(ABC):
#     @abstractmethod
#     def payment_process(self):
#         pass
#
#     def m1(self):
#         print("parent class method")
#
# class Credit_card(Payment):
#     def payment_process(self, amount):
#         print(f"using credit card pay the bill: {amount}")
#
# class UPI_payment(Payment):
#     def payment_process(self, amount):
#         print(f"using UPI pay the bill:{amount}")


# cp = Credit_card()
# cp.payment_process(600)
# cp.m1()
# upp = UPI_payment()
# upp.payment_process(1000)

# using credit card pay the bill: 600
# using UPI pay the bill:1000


# Interfaces In Python: In general if an abstract class contains only abstract methods such type of abstract class is
# considered as interface
# from abc import *
#
# class Payment(ABC):
#     @abstractmethod
#     def payment_process(self):
#         pass
#
# class Credit_card(Payment):
#     def payment_process(self, amount):
#         print(f"using credit card pay the bill: {amount}")
#
# class UPI_payment(Payment):
#     def payment_process(self, amount):
#         print(f"using UPI pay the bill:{amount}")
#
# cp = Credit_card()
# cp.payment_process(600)
# cp.m1()
# upp = UPI_payment()
# upp.payment_process(1000)

from abc import *
class DBConnection(ABC):
    @abstractmethod
    def connection(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass

class Oracle(DBConnection):
    def connection(self):
        print("Oracle Data base is connected")

    def disconnect(self):
        print("Oracle data base is disconnected..")


class MySql(DBConnection):
    def connection(self):
        print("MySql Data base is connected")

    def disconnect(self):
        print("MySql data base is disconnected..")

dbname = input("Enter DB name:")
dbclassname = globals()[dbname]
x = dbclassname()
x.connection()
x.disconnect()

# Enter DB name:MySql
# MySql Data base is connected
# MySql data base is disconnected..

config.txt file ---> inside the to write dbname


































