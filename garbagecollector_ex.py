# Garbagecollector:
#
# In old languages like C++, programmer is responsible for both creation and destruction of objects.
# Usually programmer taking very much care while creating object, but neglecting destruction of useless objects.
# Because of his neglectance, total memory can be filled with useless objects which creates memory problems and total
# application will be down with Out of memory error.
#
# But in Python, We have some assistant which is always running in the background to destroy useless objects.
# Because this assistant the chance of failing Python program with memory problems is very less.
# This assistant is nothing but Garbage Collector.
#
# Hence the main objective of Garbage Collector is to destroy useless objects.
#
# If an object does not have any reference variable then that object eligible for Garbage Collection.
#
# By default Gargbage collector is enabled, but we can disable based on our requirement.
# In this context we can use the following functions of gc module.

# 1. isenabled()
# 2. disable()
# 3. enable()

# import gc
# # print("Python garbage collector is enable or not:", gc.isenabled())
#
# gc.disable()
# print("Python garbage collector is enable or not:", gc.isenabled())
# gc.enable()
# print("Python garbage collector is enable or not:", gc.isenabled())

# Python garbage collector is enable or not: False
# Python garbage collector is enable or not: True

# Destructor: Destructor is special method and specify the name __del__
# before going to the garbagecollector allways calls to the destructors to perform cleanup activity. for example to connected to the backend
# database our application connection destrory. to perform cleanup operation.

# import gc
# import time
#
# class Test:
#
#     def __init__(self):
#         print("object Initilization...")
#
#     def __del__(self):
#         print("peform the destructor operation..")
#
# t1 = Test()
# t1 = None
# time.sleep(5)
# print("End")
# print(t1)
#
# import sys
#
# class Test:
#
#     def __init__(self):
#         print("constructure method")
#
#
# t1 = Test()
# t2 = t1
# t3 = t1
# t4 = t1
# print(sys.getrefcount(t1))
































