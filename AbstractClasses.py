# In python, if you create a class with one or more abstract methods,
# we will call it an abstract class. An abstract method is a method that will
# contain only declaration, no implementation. The class that inherits from abstract
# base class needs to implement all the base class abstract methods.
# Generally, the abstract classes are same as normal classes, but
# the only difference is the abstract classes will have one or more abstract methods.
# The abstract classes are useful when you want to provide a common interface for different
# implementations in derived classes.
# Python won’t provide direct support to the abstract classes.
# To implement abstract classes in python, you need to import the ABC (Abstract Base Classes)
# module and create the abstract methods in a base class. To create abstract methods,
# you need to create methods by decorating with the @abstractmethod attribute.

import abc #abstract base class
#class Shape(metaclass=abc.ABCMeta): #ABCMeta Class
class Shape(abc.ABC): #ABC helper class
   @abc.abstractmethod
   def area(self): #Abstract Method Declaration
      pass
class Rectangle(Shape):
   def __init__(self, x,y):
      self.l = x
      self.b=y
   def area(self):
      return self.l*self.b
r = Rectangle(10,20)
print ('area: ',r.area())