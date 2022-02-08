# # Python example to show working of multiple
# # inheritance
# class Base1(object):
#     def __init__(self):
#         self.str1 = "Class 1"
#         print ("Base1")
#
# class Base2(object):
#     def __init__(self):
#         self.str2 = "Class 2"
#         print ("Base2")
#
# class Derived(Base1, Base2):
#     def __init__(self):
#         # Calling constructors of Base1
#         # and Base2 classes
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print ("Derived Class")
#
#     def printStrs(self):
#         print(self.str1, self.str2)
#
# ob = Derived()
# ob.printStrs()

# Python example to show that base
# class members can be accessed in
# derived class using super()
class Base():

    # Constructor
    def __init__(self, x):
        self.x = x

    def sample(self):
        print("Hello base")

class Derived(Base):

    # Constructor
    def __init__(self, x, y):
        ''' In Python 3.x, "super().__init__(name)"
            also works'''
        super(Derived, self).__init__(x)
        self.y = y
        super(Derived, self).sample()

    def sample(self):
        print("Hello derived")

    def printXY(self):

    # Note that Base.x won't work here
    # because super() is used in constructor
        print(self.x, self.y)


# Driver Code
d = Derived(10, 20)
d.printXY()
#d.sample()

