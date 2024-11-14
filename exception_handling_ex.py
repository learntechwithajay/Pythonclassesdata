# Exception Handling:
# in our program occured unexpect or unwanted Errors those errors handling with help of using Exception Handling process
# in python.
# pyhton provides three types blocks:
# 1. try:
#     In our code exception raise such code we can called risky code. We have to place risky code under the try block.
#                                         (or)
#     In our code some instruction statements raise the exception. those statements place under the try block.None
# 2.except:
#   to place risky code under try block. that risky code exception handling corrsponding code has been placed in except block.
#                             (or)
#     The corresponding handling code we have to take inside except block.
#
# 3.finally: its occured exception or not occured exception to execute finally block. code repsonsible process
# we can utilize finally block

# without using try and except

# print("Statement1")
# print("division", 10/0)
# print("Statement2")
# print("Statement3")
#
# Statement1
# Traceback (most recent call last):
#   File "C:\Users\DCS\Desktop\git_repo_python_class\Pythonclassesdata\exception_handling_ex.py", line 20, in <module>
#     print("division", 10/0)
# ZeroDivisionError: division by zero

# print("Statement-1")
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter Second number:"))
# try:
#     print("Division:",num1/num2)
# except ZeroDivisionError:
#     print("Division by Zero error..")
# print("Statement - 2")
# print("Statement - 3")
# print("Statement - 4")

# Statement-1
# Enter first number:20
# Enter Second number:5
# Division: 4.0
# Statement - 2
# Statement - 3
# Statement - 4

# Statement-1
# Enter first number:20
# Enter Second number:0
# Division by Zero error..
# Statement - 2
# Statement - 3
# Statement - 4
# Normal termination/Graceful Termination


# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter Second number:"))
# try:
#     print("Sum :", num1+num2)
#     print("Division:",num1/num2)
#     print("sub:", num1-num2)
#     print("Mul:", num1*num2)
#     print("Statement - 3")
# except ZeroDivisionError:
#     print("Division by Zero error..")
# print("Statement - 4")
#
# Enter first number:20
# Enter Second number:0
# Sum : 20
# Division by Zero error..
# Statement - 4
#
# 1) Within the try block if anywhere exception raised then rest of the try block won’t be
# executed eventhough we handled that exception. Hence we have to take only risky
# code inside try block and length of the try block should be as less as possible.
# 2) In addition to try block, there may be a chance of raising exceptions inside except and
# finally blocks also.
# 3) If any statement which is not part of try block raises an exception then it is always
# abnormal termination

# try with multiple except blocks:

# try:
#     num1 = int(input("Enter first number:"))
#     num2 = int(input("Enter Second number"))
#     print("Division:", num1/num2)
# except ZeroDivisionError:
#     print("Can't divisable by zero")
# except ValueError:
#     print("Please enter integer values...")

# Enter first number:ten
# Please enter integer values...

# Enter first number:30
# Enter Second numberten
# Please enter integer values...

# Single except Block that can handle Multiple Exceptions:

try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter Second number"))
    print("Division:", num1/num2)
except (ZeroDivisionError, ValueError) as ex_msg:
    print("Please provide valid numbers and problem:", ex_msg)

# Enter first number:ten
# Please provide valid numbers and problem: invalid literal for int() with base 10: 'ten'

# Enter first number:20
# Enter Second number0
# Please provide valid numbers and problem: division by zero






























