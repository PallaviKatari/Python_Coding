# Python program to demonstrate
# use of class method and static method.
# The difference between the keywords self and cls reside only in the method type.
# If the created method is an instance method then the reserved word self has to be used,
# but if the method is a class method then the keyword cls must be used.
# Finally, if the method is a static method then none of those words will be used because as said before,
# static methods are self-contained and do not have access to the instance or class variables nor to the
# instance or class methods.

from datetime import date

class Person:
    #instance method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year. cls is used for a class method
    #We generally use class method to create factory methods.
    # Factory methods return class objects ( similar to a constructor ) for different use cases.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    #We generally use static methods to create utility functions.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('JOHN', 21)
person2 = Person.fromBirthYear('TOM', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
