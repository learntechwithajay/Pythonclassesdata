# How we can handle Overloaded Method Requirements in Python:
# Most of the times, if method with variable number of arguments required then we can
# handle with default arguments or with variable number of argument methods.

# sum method ---> user input give in different way --> single element , two or more elements

# class Test:
#     def sum(self, p1 = None, p2 = None, p3 = None):
#         total = 0
#         if p1!=None and p2!= None and p3!=None:
#             total = total + p1 + p2 + p3
#             print("Three arguments passing to the function Total is:", total)
#         elif p1!=None and p2!=None:
#             total = total + p1 + p2
#             print("TWo arguments passing to the function total is:", total)
#         elif p1!=None:
#             total = total + p1
#             print("One argument passing to the function total is :", total)
#         else:
#             print("To pass one or two or three arguments")
#
# t1 = Test()
# t1.sum(20, 30, 40)
# t1.sum(100, 200)
# t1.sum(400)
# t1.sum()

# Three arguments passing to the function Total is: 90
# TWo arguments passing to the function total is: 300
# One argument passing to the function total is : 400
# To pass one or two or three arguments

# Positional arguments --> *args --> tuple
# keyword arguments ---> **kwargs --> dictonary

# class Test:
#     def sum(self, *num):
#         total = 0
#         for n in num:
#             total = total + n
#         print("Bill Amount is:", total)
#
# t1 = Test()
# t1.sum(20, 30, 40)
# t1.sum(100, 200)
# t1.sum(400)
# t1.sum()

# Bank application having one method withdraw . this processs user done in different ways
# 1. amount
# 2. percentage
# 3. account --- another account amount transfer

class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance

    def withdraw(self, amount = None, *, percentage = None, account = None):
        if amount is not None:
            if amount <= self.balance:
                self.balance = self.balance - amount
                print(f"Withdraw {amount}. New balance:{self.balance}")
            else:
                print("Low balance...")

        elif percentage is not None:
            pamt = self.balance * (percentage/100)
            self.balance = self.balance - pamt
            print(f"Withdraw {percentage}%. New balance:{self.balance}")
        elif account is not None:
            transfer_amt = int(input("Enter Transfer Amount:"))
            if transfer_amt <= self.balance:
                self.balance = self.balance - transfer_amt
                account.balance = account.balance + transfer_amt
                print(f"Withdraw {transfer_amt}. New balance:{self.balance}")
                print(f"Transferred {transfer_amt} to {account}. New balance: {self.balance}")

            else:
                print("low balance")

act1 = BankAccount(5000)  #---> balance = 5000
act2 = BankAccount(2000)  #---> balance = 2000
act1.withdraw(amount=500)
act1.withdraw(percentage=10)
act1.withdraw(account=act2)
print("Account1 Balance is :", act1.balance)
print("Account2 Balance is :", act2.balance)


class Order:
    def __init__(self, total_amount):
        self.total_amount = total_amount

    def apply_discount(self, amount=None, *, percentage=None, promo_code=None):
        if amount is not None:
            # Fixed discount amount
            self.total_amount -= amount
            print(f"Discount of {amount} applied. New total: {self.total_amount}")

        elif percentage is not None:
            # Percentage discount
            discount = self.total_amount * (percentage / 100)
            self.total_amount -= discount
            print(f"{percentage}% discount applied. New total: {self.total_amount}")

        elif promo_code is not None:
            # Discount based on promo code
            if promo_code == "SAVE10":
                self.total_amount -= 10
                print(f"Promo code SAVE10 applied. New total: {self.total_amount}")
            elif promo_code == "HALFPRICE":
                self.total_amount /= 2
                print(f"Promo code HALFPRICE applied. New total: {self.total_amount}")

# Example Usage
order = Order(100)
order.apply_discount(amount=5)           # Fixed amount discount
order.apply_discount(percentage=10)      # Percentage discount
order.apply_discount(promo_code="SAVE10")  # Promo code discount













































