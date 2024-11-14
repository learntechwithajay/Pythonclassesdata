# Exception:
#
# Error: is nothing but a mistake in your porgramming language.
# in programming languages there are 2 types errors are possible.
# 1. Syntax Error: or compile time errors
#     your are build a instruction statement don't follow the programming language rules. its accure errors such kind of errors.
# we can called as Syntax Errors.
#
# num = 500
# class Test:
#     _a = 20
#     __b = 400
#     if num == 400
#         print("this condition is true..")

# if num == 400
# SyntaxError: invalid syntax
# Note: Programmer is responsible to correct these syntax errors. Once all syntax errors
# are corrected then only program execution will be started


# 2. Runtime Error: or Exceptions: In execution time occured errors is called Runtime errors.
# 1. User given wrong inputs to the program.
# 2. if you write any logic not reached to the application requirement.
# 3. any memory full, not supported

# Exception Handaling:
# An unwanted and unexpected event that disturbs normal flow of program is called  exception.

# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter Second number:"))
# res = num1/num2
# print(res)
# sum = num1 + num2
# sub = num1 - num2

# res = num1/num2
# ZeroDivisionError: division by zero

# num1 = int(input("Enter first number:"))
# ValueError: invalid literal for int() with base 10: 'ten'

# Example:
# ZeroDivisionError
#  TypeError
#  ValueError
#  FileNotFoundError
#  EOFError
#  SleepingError
#  TyrePuncturedError

# It is highly recommended to handle exceptions. The main objective of exception handling
# is Graceful Termination of the program (i.e we should not block our resources and we
# should not miss anything)
# Exception handling does not mean repairing exception. We have to define alternative way
# to continue rest of the program normally.
#
# Eg: For example our programming requirement is reading data from remote file locating
# at London. At runtime if London file is not available then the program should not be
# terminated abnormally. We have to provide local file to continue rest of the program
# normally. This way of defining alternative is nothing but exception handling
#
# Every exception in Python is an object. For every exception type the corresponding classes are available.
#  Whevever an exception occurs PVM will create the corresponding exception object and will check for handling code.
# If handling code is not available then Python interpreter terminates the program abnormally and prints corresponding exception
# information to the console.
#  The rest of the program won't be executed
