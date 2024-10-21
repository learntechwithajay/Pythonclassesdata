# Class and object : class is blue print an object
#  In python each every thing consider an object. its having some structure task excecute ..
# class contained represention of properties (attributes) and action (method) for object
# ---> attributes --> variables
# ---> action ---> methods
# What is syntax of class :
# class classname:
#     member variables
#     member methods or function

class Test:

    def __init__(self):
        print("Welcome to Python Class")

    def diplay(self):
        self.name = "ajay"
        self.mno = 8885565
        print(f"Name is:{self.name} \n Mobile No is: {self.mno}")

t1 = Test()
t1.diplay()
print(id(t1))
t2 = Test()
t2.diplay()
print(id(t2))

# Welcome to Python Class
# Name is:ajay
# Mobile No is: 8885565

# Object : Pysical extenestion of class is nothing object. storage local

# Welcome to Python Class
# Name is:ajay
#  Mobile No is: 8885565
# 2401239633872
# Welcome to Python Class
# Name is:ajay
#  Mobile No is: 8885565
# 2401239633680

















