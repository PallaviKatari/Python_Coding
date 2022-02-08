class car:

    def __init__(self, name, course):
        self._name = name                #protected variable
        self.course = course

    def description(self):                
        return f"{self._name} is learning {self.course}"
obj = car("John","Python")

#accessing protected variable via class method 
print(obj.description())

#accessing protected variable directly from outside
print(obj._name)
print(obj.course)
#
# class car:
#
#     def __init__(self, name, course):
#         self.__name = name                #private variable
#         self.course = course
#
#     def description(self):
#         return f"{self.__name} is learning {self.course}"
# obj = car("John","Python")
#
# #accessing protected variable via class method
# print(obj.description())
#
# #accessing protected variable directly from outside
# print(obj.__name)
# print(obj.course)
#You can still access this attribute directly using its mangled name.
# Name mangling is a mechanism we use for accessing the class members from outside.
# The Python interpreter rewrites any identifier with “__var” as “_ClassName__var”.
# And using this you can access the class member from outside as well.

class car:

    def __init__(self, name, course):
        self.__name = name                #private variable
        self.course = course

    def description(self):
        return f"{self.__name} is learning {self.course}"
obj = car("John","Python")

#accessing protected variable via class method
print(obj.description())

#accessing protected variable directly from outside
print(obj._car__name)
print(obj.course)