class Stock:
  Stock_id=1
  Quantity=1
  datetime="2.3.2024"
class Product:
    # def __init__(self):
    #     # sobject = Stock()
        # self.Stock_id = Stock.Stock_id
        # self.Quantity = Stock.Quantity
        # self.datetime = Stock.datetime

    def method(self):
        sobject = Stock()
        print("Enter Stock_id:", sobject.Stock_id)
        print("Enter Quantity:", sobject.Quantity)
        print("Enter datetime:", sobject.datetime)

c = Product()
c.method()





















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
# print(c1)
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