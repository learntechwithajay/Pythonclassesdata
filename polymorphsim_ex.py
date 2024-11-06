# Polymorphsim: is nothing but many forms : Ploy --many --> morphism -- forms
# Eg1: Yourself is best example of polymorphism.In front of Your parents You will have one
# type of behaviour and with friends another type of behaviour.Same person but different
# behaviours at different places,which is nothing but polymorphism.
# Eg2: + operator acts as concatenation and arithmetic addition
# Eg3: * operator acts as multiplication and repetition operator
# Eg4: The Same method with different implementations in Parent class and child
# classes.(overriding)
# Human --> i am in office -- my behaviour is different --> class office:
#                                                               def person:
#                                                                   print("in office...having different behaviour")
#       --> i meet the my friends --> my behaviour is different -->class Friends:
#                                                               def person:
#                                                                   print("In friends meet")
#       --> i am in class  --> my behaviour id different ---> class ClassRoom:
#                                                               def person:
#                                                                   print("In class room ")
# operators: + addition operator --> in between of two string to place + additon operator ---> ajay + kumar -->ajaykumar--> concationation
#            20 + 30 = 50 it behaviour arthematic operator
#           * --> 20 * 30 --behaviour multiplication
#             ---> 20*  --> 20*20 --> repition operators
# with Same method or function in different implementation in parent class and child class.. method overriding

# Related to Polymorphism the following 4 topics are important:
# 1) Duck Typing Philosophy of Python
# 2) Overloading
# 	1) Operator Overloading
# 	2) Method Overloading
# 	3) Constructor Overloading
# 3) Overriding
# 	1) Method Overriding
# 	2) Constructor Overriding

# Duck Typing Philosophy of Python:
# In Python we cannot specify the type explicitly. Based on provided value at
# runtime the type will be considered automatically. Hence Python is considered as
# Dynamically Typed Programming Language.
#
# --> java -->int num  --> num variable type in a compile time given memory
# ---> python --> num  -->

# class Office:
#     def person(self):
#         print("In office behaviour is different..")
#
# class Friends:
#
#     def person3(self):
#         print("In Friends meet behaviour is different..")
#
# class Home:
#
#     def person(self):
#         print("In home behaviour is different..")
#
# def fmain(tobj):
#     tobj.person()
#
# class_list = [Office(), Friends(), Home()]
#
# for obj in class_list:
#     fmain(obj)

# ofObj = Office()
# fmain(ofObj)
#
# frobj = Friends()
# fmain(frobj)

# hasattr(obj,'attributename')

# class Office:
#     def person(self):
#         print("In office behaviour is different..")
#
# class Friends:
#
#     def person3(self):
#         print("In Friends meet behaviour is different..")
#
# class Home:
#
#     def person(self):
#         print("In home behaviour is different..")
#
# def fmain(tobj):
#     if hasattr(tobj, 'person'):
#         tobj.person()
#     elif hasattr(tobj, 'person3'):
#         tobj.person3()
#
# class_list = [Office(), Friends(), Home()]
#
# for obj in class_list:
#     fmain(obj)

# class CreditCardPayment:
#     def pay(self, amount):
#         print(f"Processing credit card payment of ${amount}")
#
# class PayPalPayment:
#     def pay(self, amount):
#         print(f"Processing PayPal payment of ${amount}")
#
# class BankTransferPayment:
#     def pay(self, amount):
#         print(f"Processing bank transfer payment of ${amount}")
#
# def process_payment(payment_method, amount):
#     payment_method.pay(amount)
#
# # Using different payment methods
# process_payment(CreditCardPayment(), 50)   # Credit card payment
# process_payment(PayPalPayment(), 75)       # PayPal payment
# process_payment(BankTransferPayment(), 100)  # Bank transfer payment

class PDFGenerator:
    def generate(self, content):
        print(f"Generating PDF with content: {content}")

class WordGenerator:
    def generate(self, content):
        print(f"Generating Word document with content: {content}")

class HTMLGenerator:
    def generate(self, content):
        print(f"Generating HTML with content: {content}")

def create_document(generator, content):
    generator.generate(content)

# Using different document generators
create_document(PDFGenerator(), "Report Content")  # PDF format
create_document(WordGenerator(), "Report Content") # Word format
create_document(HTMLGenerator(), "Report Content") # HTML format

class ConsoleLogger:
    def log(self, message):
        print(f"Console log: {message}")

class FileLogger:
    def log(self, message):
        with open("log.txt", "a") as f:
            f.write(f"File log: {message}\n")

class DatabaseLogger:
    def log(self, message):
        # Imagine this logs to a database
        print(f"Database log: {message}")

def log_message(logger, message):
    logger.log(message)

# Using different loggers
log_message(ConsoleLogger(), "This is a console log message")
log_message(FileLogger(), "This is a file log message")
log_message(DatabaseLogger(), "This is a database log message")


































































