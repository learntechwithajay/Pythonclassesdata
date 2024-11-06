# class A:
#     def show(self):
#         print("A Class show method")
#
# class B(A):
#     pass
#     # def show(self):
#     #     print("B Class show method")
#
# class C(A):
#     def show(self):
#         print("C Class show method")
#
# class D(B, C):
#     pass
#
# dobj = D()
# dobj.show()
#
# # print(D.__mro__)
# print(D.mro())
#
# # B Class show method
# # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# #
# # C Class show method
# # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


Method Resolution Order (MRO):
 In Hybrid Inheritance the method resolution order is decided based on MRO
algorithm.
 This algorithm is also known as C3 algorithm.
 Samuele Pedroni proposed this algorithm.
 It follows DLR (Depth First Left to Right) i.e Child will get more priority than Parent.
 Left Parent will get more priority than Right Parent.
 MRO(X) = X+Merge(MRO(P1),MRO(P2),...,ParentList)


Head Element vs Tail Terminology:
 Assume C1,C2,C3,...are classes.
 In the list: C1C2C3C4C5....
 C1 is considered as Head Element and remaining is considered as Tail.

How to find Merge:
 Take the head of first list
 If the head is not in the tail part of any other list, then add this head to the result and
remove it from the lists in the merge.
 If the head is present in the tail part of any other list, then consider the head element
of the next list and continue the same process.
Note: We can find MRO of any class by using mro() function.
 print(ClassName.mro())
class A:
    def show(self):
        print("first method")

class B:
    def show(self):
        print("Second method")

class C:
    def show(self):
        print("Third method")

class D:
    def show(self):
        print("Four method")

class E:
    def show(self):
        print("five method")
class F(A, B, C):
    pass

class G(D, E, C):
    pass

class H(D, A):
    pass
class Z(F, G, H):
     pass

zobj = Z()
zobj.show()

print(Z.mro())

Four method
[<class '__main__.Z'>, <class '__main__.F'>, <class '__main__.G'>, <class '__main__.H'>, <class '__main__.D'>,
<class '__main__.A'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class 'object'>]

Process finished with exit code 0










































# Multi level inheriatance:
#
# class BaseClass:
#     def m1(self):
#         print("Base class method...")
#
# class ChildClass1(BaseClass):
#     def m2(self):
#         print("Child Class 1 method calling")
#
# class ChildClass2(ChildClass1):
#
#     def m3(self):
#         print("Child Class 2 method calling...")
#
# c2 = ChildClass2()
# c2.m1()
# c2.m2()
# c2.m3()







































