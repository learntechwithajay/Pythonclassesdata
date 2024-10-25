# # my Requirement is : Bank application:--> account creation ---> deposite --> withdraw --> balance ammount
# 1. bank_name
# 2. customer name, balance
# 3. deposite --method --> ammount , balance,
# 4. withdraw --> method ---> ammount, balance
# import sys
# class Customer:
#     bank_name = "SBI Bank"
#
#     def __init__(self, cname, balance = 0.0):
#         self.cname = cname
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print("Total balance amount is:", self.balance)
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficiant balance..")
#             sys.exit()
#         self.balance = self.balance - amount
#         print("Balance amount is:", self.balance)
#
# print("Welcome to", Customer.bank_name)
# cname = input("Enter Customer name:")
# c1 = Customer(cname)
# while True:
#     print("d or D - Deposit\nw or W - Withdraw\n e or E - Exit")
#     option = input("Choose above options to perform operations:")
#     if option == 'd' or option == 'D':
#         amount = float(input("Enter Deposit amount:"))
#         c1.deposit(amount)
#     elif option == 'w' or option == 'W':
#         amount = float(input("Enter withdraw amount:"))
#         c1.withdraw(amount)
#     elif option == 'e' or option == 'E':
#         print("Thanks for using SBI bank")
#         sys.exit()
#     else:
#         print("Invalid option are choose...!!")

#
# Types of methods in class:
#     1. instance method:
#
#          def m1(self):
#              self.num1 = 40
#              self.num2 = 50
#     2. class method: Inside method implementation if we are using only class variables (static variables),
#             then such type of methods we should declare as class method.
#             For class method we should provide cls variable at the time of declaration.
#             We can call classmethod by using classname or object reference variable.
#           We can declare class method explicitly by using @classmethod decorator.
#
#
#
#     class Test:
#          num1 = 100
#
#          @classmethod
#          def m1(cls):
#              print(Test.num1)
#
#
#
#
#
#
#     3. static method: its look like a general method declaration. static method inside to access static variable, instance variables
#           1. @staticmethod decorator

class Test1:
    num1 = 40

    @staticmethod
    def add(num1, y):
        res = Test1.num1 + y
        print("ADD value is:", res)

t = Test1()
t.add(Test1.num1,50)


















# local varibale:
#
#  to declare variable inside a method such kind of variables is called local varible.

# class Test:
#
#     def m1(self):
#         num = 50
#         print("Inside a method:", num)
#
# t = Test()
# t.m1()





