# super() method or function: It is builtin method, which is used to call the parent class constructure variable, and methods

# class Employee:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def display_emp(self):
#         print("Employee Name:", self.name)
#         print("Employee Salary:", self.salary)
#
# class Manager(Employee):
#     def __init__(self, name, salary, departement):
#         super().__init__(name, salary)
#         self.department = departement
#
#     def display_emp(self):
#         super().display_emp()
#         print("Department:", self.department)
#
# emp1 = Manager("Ajay kumar", 45000, "Pipeline TD")
# emp1.display_emp()

# Employee Name: Ajay kumar
# Employee Salary: 45000
# Department: Pipeline TD

# Method - 2:  parent class having static methods, class methods , static variables. how it will call child class to the parent class properties

# class TestP:
#     a = 45
#     def __init__(self):
#         self.b = 900
#
#     def m1(self):
#         print("M1 is a instance method")
#
#     @classmethod
#     def m2(cls):
#         print("M2 is a Class Method ")
#
#     @staticmethod
#     def m3():
#         print("M3 is a Static method")
#
# class TestC(TestP):
#     a = 500
#     def __init__(self):
#         self.b = 450
#         super().__init__()
#         print(super().a)
#         super().m1()
#         super().m2()
#         super().m3()
#
#     print("A Value in Child class:", a)
#
# tobj = TestC()

# 45
# M1 is a instance method
# M2 is a Class Method
# M3 is a Static method
# Method - 3: To call specific class methods
# class Test1:
#     def m1(self):
#         print("Parent class Test1")
#
# class Test2(Test1):
#     def m1(self):
#         print("Test2 class")
#
# class Test3(Test2):
#     def m1(self):
#         print("Test3 class")
#
# class Test4(Test3):
#     def m1(self):
#         print("Test4 class")
#
# class Test5(Test4):
#     def m1(self):
#         super(Test3, self).m1()
#         # Test1.m1(self)
#
#
# tobj = Test5()
# tobj.m1()
#
# Parent class Test1

# parent class instance variables are not consumed in child class instance method location

class TestP:
    num1 = 700
    def __init__(self):
        self.num2 = 560

class TestC(TestP):

    def display(self):
        print(super().num1) # valid
        # print(super().num2)  # invalid
        print(self.num2)

tobj = TestC()
tobj.display()

#     print(super().num2)
# AttributeError: 'super' object has no attribute 'num2'

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}, new balance is ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}, new balance is ${self.balance}")
        else:
            print("Insufficient funds")

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, minimum_balance=100):
        super().__init__(balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount >= self.minimum_balance:
            super().withdraw(amount)  # Call BankAccount's withdraw method
        else:
            print(f"Cannot withdraw. Minimum balance of ${self.minimum_balance} must be maintained.")

account = SavingsAccount(500, 100)
account.withdraw(450)
account.withdraw(50)
















